# 🗑️ Plataforma de Gestión de Residuos - Cartagena

Plataforma colaborativa y completa para la gestión integral de residuos en Cartagena. Permite el registro de reportes, generación automática de alertas, planificación de rutas de recolección y coordinación entre ciudadanos, operadores de aseo y administradores.

## 📋 Características

✅ **Reportes de Residuos**: Ciudadanos pueden reportar problemas de acumulación de residuos  
✅ **Alertas en Tiempo Real**: Sistema automático de alertas para operadores  
✅ **Gestión de Rutas**: Planificación y seguimiento de rutas de recolección  
✅ **Estadísticas**: Dashboard con análisis de datos  
✅ **Múltiples Roles**: Ciudadanos, Operadores, Administradores  
✅ **API REST**: Backend escalable en Python/Flask  
✅ **App Móvil**: Interfaz moderna en Flutter  

## 🗂️ Estructura del Proyecto

```
residuos-cartagena/
├── backend/              # Servidor Python/Flask
│   ├── app.py           # Aplicación principal
│   └── requirements.txt  # Dependencias
├── frontend/            # App móvil Flutter
│   ├── lib/
│   │   ├── main.dart
│   │   ├── screens/     # Pantallas de la app
│   │   ├── services/    # Servicios (API, Auth)
│   │   └── models/      # Modelos de datos
│   └── pubspec.yaml
├── database/            # Esquema y datos de BD
│   ├── schema.sql
│   └── data_ejemplo.sql
├── docs/               # Documentación
│   ├── README.md
│   ├── INSTALACION.md
│   └── API.md
└── .env                # Variables de entorno
```

## 🚀 Inicio Rápido

### Opción 1: Instalación Manual

#### Backend (Python/Flask)

```bash
# 1. Navega a la carpeta backend
cd backend

# 2. Crea un entorno virtual
python -m venv venv

# 3. Activa el entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 4. Instala dependencias
pip install -r requirements.txt

# 5. Ejecuta la aplicación
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

#### Frontend (Flutter)

```bash
# 1. Navega a la carpeta frontend
cd frontend

# 2. Obtén las dependencias
flutter pub get

# 3. Ejecuta la app
flutter run
```

### Opción 2: Con Docker (si tienes Docker instalado)

```bash
# Construir y ejecutar con docker-compose
docker-compose up --build
```

## 📱 Datos de Prueba

### Login

**Email**: juan@example.com  
**Contraseña**: pass123

Otros usuarios de prueba:
- maria@example.com (ciudadano)
- carlos@example.com (operador)
- admin@example.com (admin)

Todos con contraseña: `pass123`

## 📡 Configuración de la API

La app Flutter necesita conectarse al servidor Flask. Antes de ejecutar la app:

1. Encuentra tu IP local:
   - **Windows**: `ipconfig` → busca "Dirección IPv4"
   - **Mac/Linux**: `ifconfig` → busca "inet"

2. Edita `frontend/lib/services/api_service.dart`:
   ```dart
   static const String baseUrl = 'http://TU_IP_LOCAL:5000/api';
   ```

3. Reemplaza `TU_IP_LOCAL` con tu dirección IP

## 🗄️ Base de Datos

SQLite se crea automáticamente al iniciar el servidor. Se cargan datos de ejemplo automáticamente.

Ubicación: `database/residuos.db`

### Tablas principales:
- **usuarios**: Información de usuarios (ciudadanos, operadores, admins)
- **reportes**: Reportes de residuos
- **rutas_recoleccion**: Rutas asignadas
- **alertas**: Alertas del sistema
- **suscripciones**: Suscripciones a alertas
- **asignaciones_recoleccion**: Asignaciones de recolección

## 🔌 Endpoints API

Ver [API.md](docs/API.md) para la documentación completa.

### Autenticación

- `POST /api/auth/login` - Iniciar sesión
- `POST /api/auth/register` - Registrar usuario

### Reportes

- `GET /api/reportes` - Obtener todos
- `POST /api/reportes` - Crear nuevo
- `GET /api/reportes/<id>` - Obtener uno
- `PUT /api/reportes/<id>` - Actualizar

### Rutas

- `GET /api/rutas` - Obtener rutas
- `POST /api/rutas` - Crear ruta

### Alertas

- `GET /api/alertas` - Obtener alertas
- `GET /api/alertas/usuario/<id>` - Alertas de un usuario

### Estadísticas

- `GET /api/estadisticas` - Obtener estadísticas

## 👥 Roles del Sistema

### Ciudadano
- Crear reportes de residuos
- Ver reportes propios
- Recibir alertas sobre sus reportes
- Ver estadísticas públicas

### Operador
- Ver reportes asignados
- Ver rutas de recolección
- Actualizar estado de recolecciones
- Recibir alertas de nuevos reportes

### Administrador
- Ver todos los reportes
- Crear y gestionar rutas
- Ver estadísticas completas
- Gestionar usuarios

## 📊 Pantallas de la App

1. **Login** - Autenticación de usuarios
2. **Dashboard** - Resumen y acciones rápidas
3. **Reportes** - Ver y crear reportes
4. **Rutas** - Ver rutas de recolección
5. **Alertas** - Notificaciones del sistema
6. **Perfil** - Información del usuario

## 🔒 Seguridad

- ⚠️ **NOTA**: Esta es una versión de demostración. Para producción:
  - Implementar JWT tokens
  - Usar HTTPS
  - Encriptar contraseñas con bcrypt
  - Implementar validación de input
  - Agregar rate limiting

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+**
- **Flask** - Framework web
- **SQLite** - Base de datos
- **Flask-CORS** - CORS support

### Frontend
- **Flutter** - Framework multiplataforma
- **Provider** - State management
- **HTTP** - Cliente HTTP
- **Shared Preferences** - Almacenamiento local

## 📝 Requisitos del Proyecto

Basado en:
1. ✅ Identificar procesos actuales de recolección
2. ✅ Diseñar modelo funcional con reportes y alertas
3. ✅ Implementar prototipo completo
4. ✅ Módulos de registro, seguimiento y estadísticas
5. ✅ Rol-based access control
6. ✅ Interfaz sencilla y eficiente
7. ✅ Datos de ejemplo incluidos

## 📚 Documentación Adicional

- [Guía de Instalación Detallada](docs/INSTALACION.md)
- [Documentación de API](docs/API.md)
- [Diagramas y Diseño](docs/)

## 🤝 Contribuciones

Este es un proyecto de demostración. Siéntete libre de extenderlo y mejorarlo.

## 📞 Soporte

Para reportar errores o sugerencias, por favor crear un issue.

## ✨ Próximas Mejoras

- [ ] Integración con Google Maps
- [ ] Notificaciones push
- [ ] Geolocalización en tiempo real
- [ ] Foto de reportes
- [ ] Chat entre usuarios
- [ ] Integración con SMS
- [ ] Dashboard web
- [ ] Reportes en PDF

---

**Desarrollado para Cartagena 🇨🇴**  
Plataforma de gestión integral de residuos - 2026
