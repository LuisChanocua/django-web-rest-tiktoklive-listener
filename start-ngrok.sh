#!/bin/bash

# Script para levantar ngrok con el backend de djangoweb
# Asegúrate de tener ngrok instalado y configurado

echo "🚀 Iniciando ngrok para djangoweb Backend..."

# Verificar si ngrok está instalado
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok no está instalado. Por favor instálalo desde: https://ngrok.com/download"
    exit 1
fi

# Verificar si ngrok está configurado
if ! ngrok config check &> /dev/null; then
    echo "🔑 ngrok requiere autenticación. Por favor:"
    echo "   1. Crea una cuenta gratuita en: https://dashboard.ngrok.com/signup"
    echo "   2. Obtén tu authtoken en: https://dashboard.ngrok.com/get-started/your-authtoken"
    echo "   3. Configura ngrok con: ngrok config add-authtoken TU_AUTHTOKEN"
    echo ""
    echo "💡 Ejemplo:"
    echo "   ngrok config add-authtoken 2abc123def456ghi789jkl012mno345pqr678"
    exit 1
fi

# Verificar si el backend está corriendo en el puerto 8000
if ! curl -s http://localhost:8000 > /dev/null; then
    echo "⚠️  El backend no está corriendo en localhost:8000"
    echo "💡 Ejecuta primero: docker-compose up -d"
    echo "   O si prefieres correr sin Docker: python manage.py runserver"
    exit 1
fi

echo "✅ Backend detectado en localhost:8000"
echo "🌐 Iniciando túnel ngrok..."

# Iniciar ngrok en el puerto 8000
ngrok http 8000

echo "📝 Una vez que ngrok esté corriendo:"
echo "   1. Copia la URL HTTPS (ej: https://abc123.ngrok-free.app)"
echo "   2. Configura esta URL en Senpulse como webhook"
echo "   3. Asegúrate de que Senpulse use HTTPS para las consultas"
