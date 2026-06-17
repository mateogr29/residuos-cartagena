# 📚 Índice del Proyecto - Plataforma de Gestión de Residuos

## 🗂️ Estructura Completa

```
residuos-cartagena/
│
├── 📁 backend/                          # Servidor Python/Flask
│   ├── app.py                          # Aplicación principal (rutas API)
│   ├── requirements.txt                # Dependencias Python
│   └── venv/                           # Entorno virtual (se crea)
│
├── 📁 frontend/                         # App móvil Flutter
│   ├── lib/
│   │   ├── main.dart                   # Punto de entrada
│   │   ├── 📁 screens/
│   │   │   ├── login_screen.dart      # Pantalla de login
│   │   │   ├── register_screen.dart   # Registro de usuarios
│   │   │   ├── home_screen.dart       # Dashboard principal
│   │   │   ├── reports_screen.dart    # Gestión de reportes
│   │   │   ├── routes_screen.dart     # Ver rutas
│   │   │   ├── alerts_screen.dart     # Alertas
│   │   │   ├── statistics_screen.dart # Estadísticas
│   │   │   └── profile_screen.dart    # Perfil usuario
│   │   ├── 📁 services/
│   │   │   ├── api_service.dart       # Cliente HTTP
│   │   │   └── auth_service.dart      # Autenticación
│   │   └── 📁 models/
│   │       ├── user_model.dart        # Modelo Usuario
│   │       └── report_model.dart      # Modelo Reporte
│   ├── pubspec.yaml                    # Configuración Flutter
│   └── build/                          # Se crea al compilar
│
├── 📁 database/                         # Base de datos
│   ├── schema.sql                      # Esquema de BD
│   ├── data_ejemplo.sql                # Datos de ejemplo
│   └── residuos.db                     # BD SQLite (se crea)
│
├── 📁 docs/                             # Documentación
│   ├── README.md                       # Resumen del proyecto
│   ├── INSTALACION.md                  # Guía paso a paso
│   ├── API.md                          # Documentación de endpoints
│   ├── CONFIGURACION.md                # Configuración técnica
│   ├── QUICKSTART.md                   # Inicio rápido (5 min)
│   └── ESTRUCTURA.md                   # Este archivo
│
├── .env                                # Variables de entorno
├── .gitignore                          # Archivos a ignorar en git
└── 📄 PROYECTO_INFO.md                # Información del proyecto

```

---

## 📖 Cómo Navegar Este Proyecto

### 🏃 Si Solo Quieres Ejecutar Rápido

1. Lee: [`docs/QUICKSTART.md`](docs/QUICKSTART.md)
2. Sigue los 5 pasos en PowerShell
3. ¡Listo!

### 📚 Si Quieres Entender Todo

1. Comienza en: [`docs/README.md`](docs/README.md)
2. Luego: [`docs/INSTALACION.md`](docs/INSTALACION.md)
3. Explora: [`docs/API.md`](docs/API.md)
4. Técnica: [`docs/CONFIGURACION.md`](docs/CONFIGURACION.md)

### 💻 Si Quieres Desarrollar

1. Backend: Ve a `backend/app.py`
2. Frontend: Ve a `frontend/lib/screens/`
3. BD: Ve a `database/schema.sql`

---

## 🎯 Archivos Importantes

### Frontend (Flutter)

| Archivo | Propósito |
|---------|-----------|
| `lib/main.dart` | Punto de entrada y configuración |
| `lib/screens/login_screen.dart` | Pantalla de autenticación |
| `lib/screens/home_screen.dart` | Dashboard principal |
| `lib/services/api_service.dart` | Conexión con servidor |
| `lib/services/auth_service.dart` | Gestión de sesión |
| `pubspec.yaml` | Dependencias Flutter |

### Backend (Python)

| Archivo | Propósito |
|---------|-----------|
| `app.py` | Servidor Flask principal |
| `requirements.txt` | Dependencias Python |

### Base de Datos

| Archivo | Propósito |
|---------|-----------|
| `schema.sql` | Estructura de tablas |
| `data_ejemplo.sql` | 8 usuarios + reportes de ejemplo |

### Documentación

| Archivo | Para Leer |
|---------|-----------|
| `README.md` | Panorama general |
| `QUICKSTART.md` | Empezar en 5 minutos |
| `INSTALACION.md` | Pasos detallados |
| `API.md` | Todos los endpoints |
| `CONFIGURACION.md` | Detalles técnicos |

---

## 🚀 Flujo de Ejecución

```
1. Inicia Backend
   └─> python app.py
       ├─> Crea BD (database/residuos.db)
       ├─> Carga esquema (schema.sql)
       ├─> Inserta datos (data_ejemplo.sql)
       └─> Escucha en puerto 5000

2. Inicia Frontend
   └─> flutter run
       ├─> Carga UI (screens/)
       ├─> Se conecta a API (api_service.dart)
       └─> Espera login

3. Usuario Login
   └─> juan@example.com / pass123
       ├─> Valida en servidor
       ├─> Descarga datos
       └─> Muestra Dashboard

4. Interacción
   └─> Usuario navega por app
       ├─> Ve reportes (GET /api/reportes)
       ├─> Crea reporte (POST /api/reportes)
       ├─> Ve alertas (GET /api/alertas)
       └─> Etc.
```

---

## 📊 Requisitos del Proyecto Implementados

✅ **1. Identificar procesos actuales**
- Datos de ejemplo incluidos con reportes reales

✅ **2. Modelo funcional**
- API REST con endpoints para reportes y alertas
- Generación automática de alertas al crear reportes

✅ **3. Prototipo implementado**
- Backend completo en Python/Flask
- Frontend móvil en Flutter
- 8 pantallas funcionales

✅ **4. Módulos principales**
- Registro y login de usuarios
- Creación de reportes
- Seguimiento de rutas
- Alertas en tiempo real
- Estadísticas

✅ **5. Control por rol**
- Ciudadanos: reportan problemas
- Operadores: gestionar recolecciones
- Administradores: ver todo

✅ **6. BD con datos ejemplo**
- SQLite con 6 tablas
- 8 usuarios precargados
- 6 reportes con alertas
- 4 rutas de recolección

---

## 🔧 Tecnologías

| Componente | Tecnología | Versión |
|-----------|-----------|---------|
| **Backend** | Python/Flask | 2.3.3 |
| **Frontend** | Flutter | 3.0+ |
| **BD** | SQLite | 3 |
| **HTTP** | REST API | HTTP/1.1 |
| **State** | Provider | 6.0.0 |

---

## 🎓 Donde Empezar

### Opción 1: Ejecutar Inmediatamente
→ Ir a `docs/QUICKSTART.md`

### Opción 2: Entender Primero
→ Leer `README.md` en carpeta raíz

### Opción 3: Revisar Código
→ Explorar `frontend/lib/` y `backend/app.py`

### Opción 4: Ver API
→ Consultar `docs/API.md`

---

## 📱 Usuarios de Prueba

```
juan@example.com      / pass123  (Ciudadano)
maria@example.com     / pass123  (Ciudadano)
carlos@example.com    / pass123  (Operador)
sandra@example.com    / pass123  (Operador)
admin@example.com     / admin123 (Admin)
```

---

## ⚡ Comandos Útiles

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
flutter pub get
flutter run
```

---

## 📞 Próximas Mejoras Sugeridas

- [ ] Integración con Google Maps
- [ ] Fotos en reportes
- [ ] Notificaciones push
- [ ] Geolocalización
- [ ] Chat entre usuarios
- [ ] Dashboard web
- [ ] Exportar reportes a PDF
- [ ] Integración SMS

---

## 🎯 Resumen

Este proyecto incluye:

✨ **Backend Funcional**: Python/Flask con 18+ endpoints  
✨ **App Móvil Completa**: Flutter con 8 pantallas  
✨ **BD con Datos**: SQLite + 6 tablas + datos ejemplo  
✨ **Documentación**: 5 archivos + comentarios en código  
✨ **Usuarios Prueba**: 8 usuarios precargados  
✨ **Listo para Extender**: Arquitectura modular y limpia  

---

**Última actualización: Mayo 2026**

Happy coding! 🚀
