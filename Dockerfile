# Usar Python 3.11 como imagen base
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
        gettext \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app/

# Crear directorios necesarios
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Hacer ejecutable el script de inicio
RUN chmod +x /app/start_railway.sh

# Crear usuario no-root para seguridad
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser

# Exponer puerto
EXPOSE 8000

# Comando por defecto para desarrollo
# Para producción, Railway usará el comando del railway.json o Procfile
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
