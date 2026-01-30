# Configuración de ngrok para Senpulse

Este documento explica cómo configurar ngrok para permitir que Senpulse haga consultas a tu backend local de djangoweb.

## 📋 Prerrequisitos

1. **ngrok instalado**: Descarga desde [ngrok.com](https://ngrok.com/download)
2. **Cuenta de ngrok** (REQUERIDO desde 2024): Crea cuenta gratuita en [dashboard.ngrok.com](https://dashboard.ngrok.com/signup)
3. **Authtoken configurado**: Obtén tu token en [get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
4. **Backend corriendo** en `localhost:8000`

## 🔑 Configuración inicial de ngrok

### Paso 1: Crear cuenta gratuita
1. Ve a https://dashboard.ngrok.com/signup
2. Crea una cuenta (es completamente gratis, no requiere tarjeta de crédito)

### Paso 2: Obtener authtoken
1. Una vez registrado, ve a https://dashboard.ngrok.com/get-started/your-authtoken
2. Copia tu authtoken (algo como: `2abc123def456ghi789jkl012mno345pqr678`)

### Paso 3: Configurar ngrok
```bash
ngrok config add-authtoken TU_AUTHTOKEN_AQUI
```

**Ejemplo:**
```bash
ngrok config add-authtoken 2abc123def456ghi789jkl012mno345pqr678
```

## 🚀 Opción 1: Con Docker (Recomendado)

### Paso 1: Levantar el backend con Docker
```bash
docker-compose up -d
```

### Paso 2: Iniciar ngrok
```bash
./start-ngrok.sh
```

## 🛠️ Opción 2: Desarrollo local (sin Docker)

### Paso 1: Iniciar desarrollo con ngrok
```bash
./start-dev-ngrok.sh
```

Este script:
- Instala dependencias automáticamente
- Ejecuta migraciones
- Inicia Django en puerto 8000
- Inicia ngrok automáticamente

## 🔧 Configuración manual

Si prefieres configurar manualmente:

### 1. Instalar ngrok
```bash
# En Ubuntu/Debian
sudo snap install ngrok

# O descargar desde ngrok.com
```

### 2. Levantar el backend
```bash
# Con Docker
docker-compose up -d

# O sin Docker
python manage.py runserver 8000
```

### 3. Iniciar ngrok
```bash
ngrok http 8000
```

## 📝 Configuración en Senpulse

Una vez que ngrok esté corriendo:

1. **Copia la URL HTTPS** que ngrok te proporciona (ej: `https://abc123.ngrok-free.app`)
2. **Configura esta URL en Senpulse** como endpoint para webhooks/consultas
3. **Asegúrate de usar HTTPS** - Senpulse debe hacer requests a la URL HTTPS de ngrok

### Ejemplo de URL de webhook:
```
https://abc123.ngrok-free.app/api/senpulse/webhook/
```

## ⚙️ Configuración actualizada

El archivo `env.development` ya está configurado para:
- ✅ Permitir hosts de ngrok (`*.ngrok.io`, `*.ngrok-free.app`)
- ✅ Configurar CORS para dominios de ngrok
- ✅ Mantener configuración local para desarrollo

## 🔍 Verificar que funciona

### 1. Verificar que el backend responde
```bash
curl http://localhost:8000/api/
```

### 2. Verificar que ngrok funciona
```bash
curl https://tu-url-ngrok.ngrok-free.app/api/
```

### 3. Verificar logs de ngrok
ngrok muestra todas las requests en su interfaz web (http://localhost:4040)

## 🚨 Consideraciones importantes

### Seguridad
- ⚠️ **Solo para desarrollo**: ngrok expone tu backend local a internet
- 🔒 **No uses en producción**: Esta configuración es solo para desarrollo
- 🛡️ **Autenticación**: Asegúrate de que Senpulse use autenticación adecuada

### Limitaciones de ngrok gratuito
- 🔄 **URLs cambian**: Las URLs gratuitas cambian cada vez que reinicias ngrok
- ⏱️ **Límites de tiempo**: Sesiones limitadas a 2 horas
- 🚦 **Límites de requests**: Límites en requests por minuto

### Para URLs estables
Si necesitas una URL estable para desarrollo:
1. Crea cuenta gratuita en ngrok.com
2. Configura tu authtoken: `ngrok config add-authtoken TU_TOKEN`
3. Usa: `ngrok http 8000 --domain=tu-dominio-personalizado.ngrok-free.app`

## 🐛 Solución de problemas

### Error: "ngrok: command not found"
```bash
# Instalar ngrok
sudo snap install ngrok
# O descargar desde ngrok.com
```

### Error: "Backend no responde"
```bash
# Verificar que Docker esté corriendo
docker-compose ps

# O verificar que Django esté corriendo
curl http://localhost:8000
```

### Error de CORS
- Verifica que `CORS_ALLOWED_ORIGINS` incluya tu dominio ngrok
- Reinicia el backend después de cambios en configuración

### Error 502 Bad Gateway
- Verifica que el backend esté corriendo en puerto 8000
- Verifica que ngrok esté apuntando al puerto correcto

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs de Django: `docker-compose logs web`
2. Revisa los logs de ngrok en http://localhost:4040
3. Verifica la configuración de red y firewall
