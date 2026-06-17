# 📱 SETUP - Ejecutar en Emulador

## ✅ Backend está corriendo en:
- **Windows/Mac/Linux local:** http://192.168.1.60:5000
- **Android Emulator:** http://10.0.2.2:5000
- **iOS Simulator:** http://localhost:5000

## 📋 Credenciales de prueba (en la BD)

### Usuarios Ciudadanos
```
email: juan@example.com
password: pass123
---
email: maria@example.com
password: pass123
---
email: pedro@example.com
password: pass123
```

### Usuarios Operadores
```
email: carlos@example.com
password: pass123
---
email: sandra@example.com
password: pass123
```

### Admin
```
email: admin@example.com
password: admin123
```

## 🚀 Pasos para ejecutar:

### 1. Backend (Ya está corriendo)
El servidor Flask está corriendo en puerto 5000 con:
- Base de datos SQLite inicializada
- Datos de ejemplo cargados
- CORS habilitado para Flutter

### 2. Frontend Flutter

#### Opción A: Android Emulator
```bash
cd frontend
flutter pub get
flutter run  # O F5 en VS Code
```

Luego en la app, cambia la URL a:
- Abre `lib/services/api_service.dart`
- Cambia `baseUrl` a `http://10.0.2.2:5000/api`

#### Opción B: iOS Simulator
```bash
cd frontend
flutter pub get
flutter run -d macos  # O iPhone simulator
```

Usa: `http://localhost:5000/api`

#### Opción C: Dispositivo físico (Android/iOS)
```bash
cd frontend
flutter pub get
flutter run
```

Usa: `http://192.168.1.60:5000/api` (asegúrate de estar en la misma red Wi-Fi)

## 📡 Endpoints disponibles:

```
GET  /api/health                           → Verificar servidor
GET  /api/usuarios                         → Listar todos los usuarios
GET  /api/usuarios/<id>                    → Obtener usuario por ID
GET  /api/reportes                         → Listar todos los reportes
GET  /api/reportes/<id>                    → Obtener reporte por ID
POST /api/reportes                         → Crear nuevo reporte
PUT  /api/reportes/<id>                    → Actualizar estado de reporte
GET  /api/rutas                            → Listar rutas de recolección
POST /api/rutas                            → Crear nueva ruta
GET  /api/alertas                          → Listar alertas
GET  /api/alertas/usuario/<id>            → Alertas por usuario
GET  /api/estadisticas                     → Estadísticas generales
POST /api/auth/login                       → Login
POST /api/auth/register                    → Registro
```

## 🔧 Troubleshooting:

### ❌ "Connection refused" o "Network error"
- Verifica que el backend siga corriendo: `http://192.168.1.60:5000`
- Comprueba que estés en la misma red Wi-Fi
- Si usas Android Emulator, usa `10.0.2.2` en lugar de la IP

### ❌ "ModuleNotFoundError: No module named 'flask'"
- El backend ya tiene las dependencias instaladas
- Si necesitas reinstalar: `pip install -r requirements.txt`

### ❌ La app carga pero no muestra datos
- Verifica la URL en `api_service.dart`
- Prueba el endpoint en el navegador: `http://192.168.1.60:5000/api/usuarios`
- Revisa la consola del emulador para errores

## 📊 Datos disponibles en la BD:

- **8 usuarios**: Ciudadanos, operadores y admin
- **6 reportes de residuos**: Con diferentes tipos de urgencia
- **4 rutas de recolección**: Asignadas y en progreso
- **Estadísticas**: Conteos por tipo de residuo y urgencia

¡La app está lista para usar! 🎉
