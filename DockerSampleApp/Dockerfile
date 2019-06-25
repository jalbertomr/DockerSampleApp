# Usa runtime oficial de Python como imagen principal
FROM python:2.7-slim
# El directorio de trabajo sera /app
WORKDIR /app
# Copia el contenido actual del directorio a /app
COPY . /app
# Instala los paquetes necesarios especificados en requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#Declara puerto 80 de este contenedor disponible al mundo externo
EXPOSE 80
# Define variable de ambiente
ENV NAME Mundito (env var definido en Dockerfile)
# Ejecuta app.py cuando el contenedor se carge
CMD ["python","app.py"] 
