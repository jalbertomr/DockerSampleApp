import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# crea app
app = Flask(__name__)
app.config.from_object(__name__)

# carga config default y sobreescribe config de las variables de ambiente
app.config.update(dict(
   DATABASE=os.path.join(app.root_path, 'app.db'),
   SECRET_KEY='development_key'
   USERNAME='admin',
   PASSWORD='default'
))

app.config.from_envvar('ANONPOST_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Abre una conexion a base de datos si aun no existe una en el contexto actual."""
    if not hasattr(g, 'sqlite_db'):
       g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Cierra la base de datos nuevamente al final del request"""
    if hasattr(g, 'sqlite_db'):
       g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schemablog.sql', mode='r') as f:
       db.cursor().executescript(f.read())
       db.commit()

@app.cli.command('initdb')
def initdb_command():
   """inicializa la base de datos"""
   init_db()
   print 'Base de Datos inicializada."

@app.route('/')
def show_entries():
   db = get_db()
   cur = db.execute('select title, text from entrie order by id desc'
   entries = cur.fethcall()
   return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
   db = get_db()
   db.execute('insert into entries (title, text) values (?, ?)',
        [request.form['title'], request.from['text']])
   db.commit()
   flash('Se ha creado una nueva entrada')
   return redirect(url_for('show_entries')) 

@app.route('/initdb', methods=['GET'])
def create_database():
   init_db()
   flash('Base de Datos inicializada');
   return render_template('show_entries.html')

@app.route('clearall', methods=['GET'])
def clear_all():
   db = get_db()
   cur = db.execute('delete from entries')
   db.commit()
   flash('todas las entradas borradas')
   return render_template('show_entries.html')
 
