# Guía de Despliegue en Railway

Esta guía te ayudará a desplegar tu aplicación Django djangoweb en Railway.

## Prerrequisitos

1. Cuenta en [Railway](https://railway.app)
2. Repositorio en GitHub/GitLab
3. Configuración de Kinde y SendPulse (opcional)

## Paso 1: Crear Proyecto en Railway

1. Ve a [Railway](https://railway.app) y haz login
2. Haz clic en "New Project"
3. Selecciona "Deploy from GitHub repo"
4. Conecta tu repositorio y selecciona `djangoweb-backend`

## Paso 2: Configurar Base de Datos PostgreSQL

1. En tu proyecto de Railway, haz clic en "New"
2. Selecciona "Database" → "PostgreSQL"
3. Railway creará automáticamente las variables de entorno:
   - `DATABASE_URL`
   - `PGHOST`
   - `PGPORT`
   - `PGUSER`
   - `PGPASSWORD`
   - `PGDATABASE`

## Paso 3: Configurar Redis (Opcional)

Si usas Celery, necesitarás Redis:

1. En tu proyecto de Railway, haz clic en "New"
2. Selecciona "Database" → "Redis"
3. Railway creará automáticamente las variables de entorno:
   - `REDIS_URL`

## Paso 4: Configurar Variables de Entorno

En la pestaña "Variables" de tu servicio principal, configura:

### Variables Obligatorias
```
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-segura
ALLOWED_HOSTS=*.railway.app,tu-dominio-personalizado.com
RAILWAY_ENVIRONMENT=True
```

### Variables de Base de Datos (Automáticas)
Railway crea automáticamente `DATABASE_URL`. No necesitas configurar variables individuales.

### Variables de Redis (Si usas Celery)
```
CELERY_BROKER_URL=redis://default:password@containers-us-west-xxx.railway.app:6379
CELERY_RESULT_BACKEND=redis://default:password@containers-us-west-xxx.railway.app:6379
```

### Variables de CORS
```
CORS_ALLOWED_ORIGINS=https://tu-app.railway.app,https://tu-dominio-personalizado.com
```

## Paso 5: Configurar Comando de Inicio

Railway usará automáticamente el `railway.json` o `Procfile` que ya están configurados.

## Paso 6: Migraciones Automáticas

Las migraciones se ejecutan automáticamente gracias a la configuración en `railway.json` y `Procfile`. El proceso incluye:

1. **Migraciones de base de datos** - `python manage.py migrate`
2. **Recopilación de archivos estáticos** - `python manage.py collectstatic --noinput`
3. **Inicio del servidor** - `gunicorn`

### Healthcheck
Railway verificará que la aplicación esté funcionando en `/health/` que devuelve:
```json
{
  "status": "healthy",
  "environment": "production",
  "debug": "False"
}
```

## Paso 7: Configurar Dominio Personalizado (Opcional)

1. En la pestaña "Settings" de tu servicio
2. Ve a "Domains"
3. Agrega tu dominio personalizado
4. Configura los registros DNS según las instrucciones de Railway

## Paso 8: Configurar Workers (Si usas Celery)

Si necesitas workers de Celery:

1. Crea un nuevo servicio en Railway
2. Usa el mismo código fuente
3. Configura el comando de inicio como:
   ```
   celery -A djangoweb_backend worker --loglevel=info
   ```

## Paso 9: Configurar Beat (Si usas Celery Beat)

Para tareas programadas:

1. Crea otro servicio en Railway
2. Usa el mismo código fuente
3. Configura el comando de inicio como:
   ```
   celery -A djangoweb_backend beat --loglevel=info
   ```

## Verificación del Despliegue

1. Ve a la URL de tu aplicación (algo como `https://tu-app.railway.app`)
2. Verifica que la aplicación responda correctamente
3. Revisa los logs para asegurarte de que no hay errores

## Comandos Útiles

### Ver logs en tiempo real
```bash
railway logs
```

### Conectar a la base de datos
```bash
railway connect postgres
```

### Ejecutar comandos Django
```bash
railway run python manage.py shell
railway run python manage.py createsuperuser
```

## Solución de Problemas

### Error de migraciones
- Asegúrate de que las variables de base de datos estén configuradas
- Ejecuta `python manage.py migrate` manualmente

### Error de CORS
- Verifica que `CORS_ALLOWED_ORIGINS` incluya tu dominio de Railway
- Asegúrate de que `ALLOWED_HOSTS` esté configurado correctamente

### Error de archivos estáticos
- Ejecuta `python manage.py collectstatic --noinput`
- Verifica que `STATIC_ROOT` esté configurado en settings.py

### Error de Celery
- Verifica que `CELERY_BROKER_URL` y `CELERY_RESULT_BACKEND` estén configurados
- Asegúrate de que Redis esté funcionando

## Monitoreo

Railway proporciona métricas básicas en el dashboard. Para monitoreo avanzado, considera integrar servicios como:
- Sentry para errores
- New Relic para performance
- LogRocket para debugging

## Costos

Railway ofrece un plan gratuito con límites. Revisa los precios actuales en su sitio web.

---

¡Tu aplicación Django djangoweb debería estar funcionando en Railway! 🚀
