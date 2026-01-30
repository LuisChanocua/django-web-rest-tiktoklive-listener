#!/bin/bash

# Script para iniciar el proyecto djangoweb con Docker

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN} Iniciando djangoweb Backend con Docker...${NC}"

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker no está instalado. Por favor instala Docker primero.${NC}"
    exit 1
fi

# Verificar si Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose no está instalado. Por favor instala Docker Compose primero.${NC}"
    exit 1
fi

# Función para mostrar ayuda
show_help() {
    echo -e "${YELLOW}Uso: $0 [comando]${NC}"
    echo ""
    echo "Comandos disponibles:"
    echo "  dev       - Iniciar en modo desarrollo"
    echo "  prod      - Iniciar en modo producción"
    echo "  build     - Construir las imágenes"
    echo "  stop      - Detener todos los contenedores"
    echo "  restart   - Reiniciar todos los contenedores"
    echo "  logs      - Ver logs de todos los contenedores"
    echo "  shell     - Abrir shell en el contenedor web"
    echo "  migrate   - Ejecutar migraciones"
    echo "  createsuperuser - Crear superusuario"
    echo "  clean     - Limpiar contenedores y volúmenes"
    echo "  help      - Mostrar esta ayuda"
}

# Función para limpiar
clean_docker() {
    echo -e "${YELLOW}🧹 Limpiando contenedores y volúmenes...${NC}"
    docker-compose down -v
    docker system prune -f
    echo -e "${GREEN}✅ Limpieza completada${NC}"
}

# Función para ejecutar comando en contenedor web
run_in_web() {
    docker-compose exec web "$@"
}

# Función para verificar archivos .env
check_env_files() {
    if [ ! -f "env.development" ]; then
        echo -e "${RED}❌ Archivo env.development no encontrado${NC}"
        echo -e "${YELLOW}💡 Copia env.example a env.development y configura las variables${NC}"
        exit 1
    fi
    
    if [ ! -f "env.production" ]; then
        echo -e "${YELLOW}⚠️  Archivo env.production no encontrado${NC}"
        echo -e "${YELLOW}💡 Copia env.example a env.production y configura las variables para producción${NC}"
    fi
}

# Procesar argumentos
case "${1:-dev}" in
    "dev")
        echo -e "${GREEN}🚀 Iniciando en modo desarrollo...${NC}"
        check_env_files
        docker-compose up --build
        ;;
    "prod")
        echo -e "${GREEN}🚀 Iniciando en modo producción...${NC}"
        check_env_files
        docker-compose -f docker-compose.prod.yml up --build -d
        ;;
    "build")
        echo -e "${YELLOW}🔨 Construyendo imágenes...${NC}"
        docker-compose build
        ;;
    "stop")
        echo -e "${YELLOW}⏹️  Deteniendo contenedores...${NC}"
        docker-compose down
        ;;
    "restart")
        echo -e "${YELLOW}🔄 Reiniciando contenedores...${NC}"
        docker-compose restart
        ;;
    "logs")
        echo -e "${YELLOW}📋 Mostrando logs...${NC}"
        docker-compose logs -f
        ;;
    "shell")
        echo -e "${YELLOW}🐚 Abriendo shell en contenedor web...${NC}"
        run_in_web bash
        ;;
    "migrate")
        echo -e "${YELLOW}🗄️  Ejecutando migraciones...${NC}"
        run_in_web python manage.py migrate
        ;;
    "createsuperuser")
        echo -e "${YELLOW}👤 Creando superusuario...${NC}"
        run_in_web python manage.py createsuperuser
        ;;
    "clean")
        clean_docker
        ;;
    "help"|"-h"|"--help")
        show_help
        ;;
    *)
        echo -e "${RED}❌ Comando no reconocido: $1${NC}"
        show_help
        exit 1
        ;;
esac
