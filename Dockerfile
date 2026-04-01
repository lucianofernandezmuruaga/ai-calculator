# Usamos una imagen liviana de Python
FROM python:3.11-slim

# Seteamos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos primero (buena práctica de caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos nuestro script al contenedor
#COPY calculator.py .

# Copiamos todo el contenido de nuestra carpeta local a /app
COPY . .

# Ejecutamos el script cuando el contenedor arranque
CMD ["python", "src/calculator.py"]