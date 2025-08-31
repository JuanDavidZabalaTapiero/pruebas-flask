# Imagen base de Python
FROM python:3.11-slim

# Instalar dependencias de sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Variables de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Puerto de Flask
EXPOSE 5000

# Comando por defecto
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]