# 🔧 Configuración de Variables de Entorno - djangoweb Backend

Este documento explica cómo configurar las variables de entorno para el proyecto djangoweb Backend.

## 📁 Archivos de Configuración

### Archivos Disponibles

- **`env.example`** - Plantilla con todas las variables disponibles
- **`env.development`** - Configuración para desarrollo (ya creado)
- **`env.production`** - Configuración para producción (ya creado)
- **`env.docker`** - Configuración específica para Docker (legacy)

## 🚀 Configuración Inicial

### 1. Copiar Archivos de Configuración

```bash
# Para desarrollo
cp env.example .env

# O usar los archivos específicos ya creados
cp env.development .env
```

### 2. Configurar Variables

Edita el archivo `.env` (o `env.development`/`env.production`) con tus valores:

```bash
# Configuración básica
DEBUG=True
SECRET_KEY=tu-secret-key-super-seguro
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Base de datos
DB_NAME=djangoweb_db
DB_USER=postgres
DB_PASSWORD=tu-password-seguro
DB_HOST=db
DB_PORT=5432

# Redis
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Configuración de Nicknames
NICKNAME_MAX_LENGTH=30
NICKNAME_MIN_LENGTH=3
NICKNAME_GENERATION_MAX_ATTEMPTS=100

# Docker
DOCKER_CONTAINER=True
```

## 🐳 Uso con Docker

### Desarrollo

```bash
# Usar archivo env.development
docker-compose up --build

# O usar archivo .env personalizado
docker-compose --env-file .env up --build
```

### Producción

```bash
# Usar archivo env.production
docker-compose -f docker-compose.prod.yml up --build -d

# O usar archivo .env personalizado
docker-compose -f docker-compose.prod.yml --env-file .env up --build -d
```

## 🔒 Seguridad

### Variables Sensibles

**NUNCA** commitees archivos `.env` con datos reales:

```bash
# .gitignore ya incluye:
.env
*.env
!env.example
!env.development
!env.production
```

### Variables de Producción

Para producción, usa variables de entorno del sistema o un gestor de secretos:

```bash
# En el servidor
export SECRET_KEY="tu-secret-key-super-seguro"
export DB_PASSWORD="tu-password-super-seguro"
export KINDE_CLIENT_SECRET="tu-client-secret"
```

## 📋 Variables Disponibles

### Configuración Básica

| Variable | Descripción | Desarrollo | Producción |
|----------|-------------|------------|------------|
| `DEBUG` | Modo debug | `True` | `False` |
| `SECRET_KEY` | Clave secreta de Django | Cambiar | Cambiar |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1,0.0.0.0` | Tu dominio |

### Base de Datos

| Variable | Descripción | Desarrollo | Producción |
|----------|-------------|------------|------------|
| `DB_NAME` | Nombre de la base de datos | `djangoweb_db` | `djangoweb_prod` |
| `DB_USER` | Usuario de la base de datos | `postgres` | `djangoweb_user` |
| `DB_PASSWORD` | Contraseña de la base de datos | `postgres123` | Cambiar |
| `DB_HOST` | Host de la base de datos | `db` | `db` |
| `DB_PORT` | Puerto de la base de datos | `5432` | `5432` |

### CORS

| Variable | Descripción | Desarrollo | Producción |
|----------|-------------|------------|------------|
| `CORS_ALLOWED_ORIGINS` | Orígenes permitidos para CORS | `http://localhost:3000,http://127.0.0.1:3000` | `https://tu-dominio.com` |

### Docker

| Variable | Descripción | Valor |
|----------|-------------|-------|
| `DOCKER_CONTAINER` | Indica si está en contenedor | `True` |

## 🛠️ Comandos Útiles

### Verificar Variables

```bash
# Ver todas las variables cargadas
docker-compose exec web env | grep -E "(DEBUG|DB_|CELERY_|KINDE_)"

# Ver variables específicas
docker-compose exec web env | grep SECRET_KEY
```

### Recargar Variables

```bash
# Parar y reiniciar con nuevas variables
docker-compose down
docker-compose up --build
```

### Debug de Variables

```bash
# Ver logs de configuración
docker-compose logs web | grep -i "setting"
```

## 🔧 Troubleshooting

### Error: Variable no encontrada

```bash
# Verificar que el archivo .env existe
ls -la .env

# Verificar que la variable está definida
grep VARIABLE_NAME .env
```

### Error: Archivo .env no encontrado

```bash
# Crear archivo .env desde plantilla
cp env.example .env

# O usar archivo específico
cp env.development .env
```

### Error: Permisos de archivo

```bash
# Dar permisos de lectura
chmod 644 .env
```

## 📚 Referencias

- [Django Settings](https://docs.djangoproject.com/en/stable/topics/settings/)
- [Docker Compose Environment Variables](https://docs.docker.com/compose/environment-variables/)
- [python-decouple](https://github.com/henriquebastos/python-decouple)
