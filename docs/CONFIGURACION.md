# ⚙️ Configuración del Proyecto

## 🖥️ Entorno de Desarrollo

### Backend (Python/Flask)

**Archivo**: `backend/app.py`

Configuraciones principales:
```python
DATABASE = os.path.join(os.path.dirname(__file__), '..', 'database', 'residuos.db')
DEBUG = True  # Cambiar a False en producción
```

**Puerto**: 5000
**Host**: 0.0.0.0 (accesible desde la red)

### Frontend (Flutter)

**Archivo**: `frontend/lib/services/api_service.dart`

```dart
static const String baseUrl = 'http://192.168.1.100:5000/api';
```

Reemplaza la IP con la de tu máquina local.

## 📊 Base de Datos

**Tipo**: SQLite  
**Ubicación**: `database/residuos.db`

Se crea automáticamente al iniciar el servidor.

### Tablas Principales

1. **usuarios** - Información de usuarios
   - id, nombre, email, password, rol, telefono, imagen_perfil, estado

2. **reportes** - Reportes de residuos
   - id, usuario_id, titulo, descripcion, ubicacion, latitud, longitud, tipo_residuo, nivel_urgencia, estado, imagen_url

3. **rutas_recoleccion** - Rutas de recolección
   - id, operador_id, estado, fecha_asignacion, hora_estimada, zonas_cobertura, ubicacion_inicio, ubicacion_fin

4. **alertas** - Alertas del sistema
   - id, reporte_id, mensaje, tipo_alerta, estado, fecha_creacion, fecha_lectura

5. **suscripciones** - Suscripciones a alertas
   - id, usuario_id, alerta_id, tipo_notificacion, estado

6. **asignaciones_recoleccion** - Asignaciones de recolección
   - id, ruta_id, reporte_id, operador_id, estado, fecha_asignacion, fecha_confirmacion

## 🔑 Variables de Entorno

Edita `.env` para configurar:

```env
API_BASE_URL=http://192.168.1.100:5000
API_PORT=5000
API_HOST=0.0.0.0
DATABASE_NAME=residuos.db
FLASK_ENV=development
FLASK_DEBUG=True
```

## 🚀 Comandos Útiles

### Backend

```bash
# Activar entorno virtual
venv\Scripts\activate          # Windows
source venv/bin/activate      # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python app.py

# Salir del entorno virtual
deactivate
```

### Frontend

```bash
# Obtener dependencias
flutter pub get

# Ejecutar en dispositivo
flutter run

# Build para Android
flutter build apk

# Build para iOS
flutter build ios

# Build para Web
flutter build web

# Clean
flutter clean
```

## 📈 Arquitectura

```
┌─────────────────────────────────────────────┐
│         APP MÓVIL (Flutter)                 │
│  ┌────────────────────────────────────┐    │
│  │ Screens (UI/UX)                    │    │
│  │ ├── Login / Register               │    │
│  │ ├── Dashboard                      │    │
│  │ ├── Reportes                       │    │
│  │ ├── Rutas                          │    │
│  │ ├── Alertas                        │    │
│  │ └── Perfil                         │    │
│  └────────────────────────────────────┘    │
│  ┌────────────────────────────────────┐    │
│  │ Services                           │    │
│  │ ├── AuthService                    │    │
│  │ └── ApiService                     │    │
│  └────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
            ↓ HTTP/REST ↓
┌─────────────────────────────────────────────┐
│    SERVIDOR API (Python/Flask)              │
│  ┌────────────────────────────────────┐    │
│  │ Rutas (Endpoints)                  │    │
│  │ ├── /api/auth/*                    │    │
│  │ ├── /api/reportes/*                │    │
│  │ ├── /api/rutas/*                   │    │
│  │ ├── /api/alertas/*                 │    │
│  │ └── /api/estadisticas              │    │
│  └────────────────────────────────────┘    │
│  ┌────────────────────────────────────┐    │
│  │ Servicios de Negocio               │    │
│  │ ├── Gestión de reportes            │    │
│  │ ├── Alertas automáticas            │    │
│  │ └── Estadísticas                   │    │
│  └────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
            ↓ SQL ↓
┌─────────────────────────────────────────────┐
│    BASE DE DATOS (SQLite)                   │
│  ├── usuarios                               │
│  ├── reportes                               │
│  ├── rutas_recoleccion                      │
│  ├── alertas                                │
│  └── suscripciones                          │
└─────────────────────────────────────────────┘
```

## 🔐 Seguridad (Notas Importantes)

⚠️ **Versión de Desarrollo**: Esta plataforma es una demostración.

Para **Producción**, necesitarías:

1. **Autenticación**
   - Implementar JWT tokens
   - Usar refresh tokens
   - Encriptar contraseñas con bcrypt

2. **Comunicación**
   - HTTPS en lugar de HTTP
   - Certificados SSL/TLS
   - API key authentication

3. **Base de datos**
   - Usar PostgreSQL o MySQL
   - Implementar backups
   - Configurar usuarios con permisos

4. **Validación**
   - Input validation
   - Rate limiting
   - CORS configuration
   - SQL injection prevention

5. **Logging**
   - Registrar acciones
   - Auditoría de cambios
   - Monitoreo de errores

## 🧪 Testing

Actualmente no hay tests automatizados. Para agregar:

```bash
# Python (unittest)
python -m unittest discover -s tests

# Flutter
flutter test
```

## 📱 Requisitos Mínimos del Sistema

**Backend:**
- Python 3.8+
- 100 MB disco
- 512 MB RAM

**Frontend:**
- Android 5.0+ o iOS 11+
- 100 MB almacenamiento
- Conexión a red local

## 📞 Debugging

### Backend Logs

Abre el terminal donde corre Flask para ver logs:
```
[2026-05-05 10:30:00] GET /api/health 200
[2026-05-05 10:30:05] POST /api/auth/login 200
```

### Frontend Logs

En Flutter, usa:
```bash
flutter run -v  # Modo verbose
```

### Database Inspector

Para explorar la BD:
```bash
# Instala DB Browser for SQLite
# https://sqlitebrowser.org/

# O usa sqlite3 desde terminal
sqlite3 database/residuos.db
```

## 📚 Recursos Útiles

- [Flutter Docs](https://flutter.dev/docs)
- [Flask Docs](https://flask.palletsprojects.com/)
- [SQLite Docs](https://www.sqlite.org/docs.html)
- [HTTP Package](https://pub.dev/packages/http)

---

**Última actualización: Mayo 2026**
