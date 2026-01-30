# djangoweb Backend - Docker Setup

Este documento explica cómo ejecutar el proyecto djangoweb Backend usando Docker.

## 📋 Requisitos Previos

- Docker (versión 20.10 o superior)
- Docker Compose (versión 2.0 o superior)

### Instalación de Docker

#### Ubuntu/Debian:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### Windows:
Descargar Docker Desktop desde [docker.com](https://www.docker.com/products/docker-desktop)

#### macOS:
Descargar Docker Desktop desde [docker.com](https://www.docker.com/products/docker-desktop)

## 🚀 Inicio Rápido

### Opción 1: Usando el script de inicio (Recomendado)

```bash
# Hacer el script ejecutable (solo la primera vez)
chmod +x docker-start.sh

# Iniciar en modo desarrollo
./docker-start.sh dev

# O iniciar en modo producción
./docker-start.sh prod
```

### Opción 2: Usando Docker Compose directamente

#### Modo Desarrollo:
```bash
# Construir e iniciar todos los servicios
docker-compose up --build

# O en segundo plano
docker-compose up --build -d
```

#### Modo Producción:
```bash
# Usar el archivo de configuración de producción
docker-compose -f docker-compose.prod.yml up --build -d
```

## 🛠️ Comandos Disponibles

### Script de Inicio (`./docker-start.sh`)

| Comando | Descripción |
|---------|-------------|
| `dev` | Iniciar en modo desarrollo |
| `prod` | Iniciar en modo producción |
| `build` | Construir las imágenes |
| `stop` | Detener todos los contenedores |
| `restart` | Reiniciar todos los contenedores |
| `logs` | Ver logs de todos los contenedores |
| `shell` | Abrir shell en el contenedor web |
| `migrate` | Ejecutar migraciones |
| `createsuperuser` | Crear superusuario |
| `clean` | Limpiar contenedores y volúmenes |
| `help` | Mostrar ayuda |

### Comandos Docker Compose

```bash
# Ver estado de los contenedores
docker-compose ps

# Ver logs de un servicio específico
docker-compose logs web
docker-compose logs db
docker-compose logs redis

# Ejecutar comandos en el contenedor web
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v
```

## 🏗️ Arquitectura de Servicios

### Servicios Incluidos

1. **web** - Aplicación Django
   - Puerto: 8000
   - Comando: `python manage.py runserver 0.0.0.0:8000` (dev) / `gunicorn` (prod)

2. **db** - Base de datos PostgreSQL
   - Puerto: 5432
   - Base de datos: `djangoweb_db`
   - Usuario: `postgres`
   - Contraseña: `postgres123`

## ⚙️ Configuración

### Variables de Entorno

El proyecto usa las siguientes variables de entorno:

```bash
# Configuración básica
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Base de datos
DB_NAME=djangoweb_db
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=db
DB_PORT=5432

```

### Archivos de Configuración

- `docker-compose.yml` - Configuración para desarrollo
- `docker-compose.prod.yml` - Configuración para producción
- `env.docker` - Variables de entorno para Docker
- `Dockerfile` - Imagen de la aplicación

## 🗄️ Base de Datos

### Migraciones

```bash
# Ejecutar migraciones
./docker-start.sh migrate

# O manualmente
docker-compose exec web python manage.py migrate
```

### Crear Superusuario

```bash
# Crear superusuario
./docker-start.sh createsuperuser

# O manualmente
docker-compose exec web python manage.py createsuperuser
```

### Acceso a la Base de Datos

```bash
# Conectar a PostgreSQL
docker-compose exec db psql -U postgres -d djangoweb_db

# O desde el host (si tienes psql instalado)
psql -h localhost -p 5432 -U postgres -d djangoweb_db
```

## 📁 Volúmenes

### Volúmenes de Datos

- `postgres_data` - Datos de PostgreSQL
- `static_volume` - Archivos estáticos
- `media_volume` - Archivos de media

### Montaje de Código

En desarrollo, el código se monta como volumen para cambios en tiempo real.

## 🔧 Desarrollo

### Estructura de Archivos

```
djangoweb-backend/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── .dockerignore
├── docker-start.sh
├── env.docker
├── requirements.txt
└── ...
```

### Hot Reload

En modo desarrollo, los cambios en el código se reflejan automáticamente sin necesidad de reconstruir la imagen.

### Debugging

```bash
# Ver logs en tiempo real
docker-compose logs -f web

# Acceder al shell del contenedor
docker-compose exec web bash

# Ver procesos en ejecución
docker-compose exec web ps aux
```

## 🚀 Producción

### Configuración de Producción

1. Crear archivo `.env` con variables de producción
2. Usar `docker-compose.prod.yml`
3. Configurar proxy reverso (nginx) si es necesario

### Variables de Producción

```bash
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_PASSWORD=your-secure-password
```

### Despliegue

```bash
# Construir y desplegar
docker-compose -f docker-compose.prod.yml up --build -d

# Verificar estado
docker-compose -f docker-compose.prod.yml ps

# Ver logs
docker-compose -f docker-compose.prod.yml logs -f
```

## 🧹 Mantenimiento

### Limpieza

```bash
# Limpiar contenedores y volúmenes
./docker-start.sh clean

# O manualmente
docker-compose down -v
docker system prune -f
```

### Backup de Base de Datos

```bash
# Crear backup
docker-compose exec db pg_dump -U postgres djangoweb_db > backup.sql

# Restaurar backup
docker-compose exec -T db psql -U postgres djangoweb_db < backup.sql
```

### Actualización

```bash
# Detener servicios
docker-compose down

# Actualizar código
git pull

# Reconstruir y reiniciar
docker-compose up --build -d
```

## 🐛 Solución de Problemas

### Problemas Comunes

1. **Puerto ya en uso**
   ```bash
   # Cambiar puerto en docker-compose.yml
   ports:
     - "8001:8000"  # Usar puerto 8001 en lugar de 8000
   ```

2. **Error de permisos**
   ```bash
   # Dar permisos al script
   chmod +x docker-start.sh
   ```

3. **Base de datos no conecta**
   ```bash
   # Verificar que el servicio db esté corriendo
   docker-compose ps
   
   # Reiniciar servicios
   docker-compose restart
   ```

4. **Volúmenes corruptos**
   ```bash
   # Limpiar volúmenes
   docker-compose down -v
   docker volume prune -f
   ```

### Logs de Debug

```bash
# Ver logs detallados
docker-compose logs --tail=100 -f web

# Ver logs de todos los servicios
docker-compose logs --tail=50 -f
```

## 📚 Recursos Adicionales

- [Documentación de Docker](https://docs.docker.com/)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)
- [Django en Docker](https://docs.djangoproject.com/en/stable/howto/deployment/docker/)
- [PostgreSQL en Docker](https://hub.docker.com/_/postgres)
- [Redis en Docker](https://hub.docker.com/_/redis)

## 🤝 Contribución

Para contribuir al proyecto:

1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer los cambios necesarios
4. Probar con Docker
5. Crear un Pull Request

## 📞 Soporte

Si tienes problemas con la configuración de Docker, por favor:

1. Revisar los logs: `docker-compose logs`
2. Verificar la documentación
3. Crear un issue en el repositorio
