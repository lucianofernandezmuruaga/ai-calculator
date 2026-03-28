# Usamos una imagen liviana de Python
FROM python:3.11-slim

# Seteamos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos nuestro script al contenedor
COPY calculator.py .

# Ejecutamos el script cuando el contenedor arranque
CMD ["python", "calculator.py"]