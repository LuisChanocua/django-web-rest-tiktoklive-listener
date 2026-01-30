#!/bin/bash

# Script para desarrollo local con ngrok (sin Docker)
# Útil para desarrollo rápido sin contenedores

echo "🚀 Iniciando desarrollo local con ngrok..."

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

# Verificar si Python está disponible
if ! command -v python &> /dev/null; then
    echo "❌ Python no está instalado"
    exit 1
fi

# Verificar si las dependencias están instaladas
if [ ! -f "requirements.txt" ]; then
    echo "❌ No se encontró requirements.txt"
    exit 1
fi

echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "🗄️  Ejecutando migraciones..."
python manage.py migrate

echo "🌐 Iniciando servidor Django en puerto 8000..."
# Iniciar Django en background
python manage.py runserver 8000 &
DJANGO_PID=$!

# Esperar un momento para que Django inicie
sleep 3

echo "✅ Django iniciado (PID: $DJANGO_PID)"
echo "🌐 Iniciando túnel ngrok..."

# Función para limpiar procesos al salir
cleanup() {
    echo "🛑 Deteniendo procesos..."
    kill $DJANGO_PID 2>/dev/null
    exit 0
}

# Capturar Ctrl+C
trap cleanup SIGINT

# Iniciar ngrok
ngrok http 8000

# Limpiar al salir
cleanup
