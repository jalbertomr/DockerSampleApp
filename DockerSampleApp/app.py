from flask import Flask
from redis import Redis, RedisError
import redis
import os
import socket

# Conectar a Redis
# redis = Redis.Redis(host='localhost', port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)
redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
       visits = redis_conn.incr("counter")
    except RedisError:
     visits = "<i>No hay conexion con Redis, contador deshabilidado</i>"
    html = "<h3>Hola variable entorno NAME={name}!</h3>" \
         "<b>Hostname:</b> {hostname}<br/>" \
         "<b>Visitas:</b> {visits}"

    return html.format(name=os.getenv("NAME", "valordefault"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)

