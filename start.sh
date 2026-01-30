#!/bin/bash

# Script de inicio para Railway
# Este script se ejecuta automáticamente al desplegar

echo "🚀 Iniciando djangoweb Backend en Railway..."

# Verificar variables de entorno críticas
echo "🔍 Verificando variables de entorno..."
if [ -z "$SECRET_KEY" ]; then
    echo "❌ ERROR: SECRET_KEY no está configurada"
    exit 1
fi

if [ -z "$DATABASE_URL" ] && [ -z "$DB_HOST" ]; then
    echo "❌ ERROR: No hay configuración de base de datos"
    exit 1
fi

echo "✅ Variables de entorno verificadas"

# Ejecutar migraciones
echo "📊 Ejecutando migraciones de base de datos..."
python manage.py migrate --noinput

# Recopilar archivos estáticos
echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Verificar que la aplicación puede iniciar
echo "🔧 Verificando configuración de Django..."
python manage.py check --deploy

# Iniciar la aplicación con Gunicorn
echo "🌐 Iniciando servidor con Gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 djangoweb_backend.wsgi:application
