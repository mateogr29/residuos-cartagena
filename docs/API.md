# 📡 Documentación de API REST

Base URL: `http://localhost:5000/api` o `http://TU_IP:5000/api`

## 🔐 Autenticación

### Login

**POST** `/auth/login`

Inicia sesión en la plataforma.

**Request:**
```json
{
  "email": "juan@example.com",
  "password": "pass123"
}
```

**Response (200):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "nombre": "Juan Rodríguez",
    "email": "juan@example.com",
    "rol": "ciudadano",
    "imagen_perfil": "https://..."
  }
}
```

**Response (401):**
```json
{
  "success": false,
  "message": "Credenciales inválidas"
}
```

---

### Registro

**POST** `/auth/register`

Registra un nuevo usuario.

**Request:**
```json
{
  "nombre": "Pedro García",
  "email": "pedro@example.com",
  "password": "micontraseña123",
  "telefono": "3001234567"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Usuario registrado exitosamente",
  "user_id": 9
}
```

---

## 📝 Reportes

### Obtener Todos los Reportes

**GET** `/reportes`

Obtiene todos los reportes del sistema.

**Response (200):**
```json
[
  {
    "id": 1,
    "usuario_id": 1,
    "titulo": "Acumulación de residuos en Bazurto",
    "descripcion": "Hay una gran cantidad de residuos...",
    "ubicacion": "Bazurto, Cartagena",
    "latitud": 10.3932,
    "longitud": -75.5136,
    "tipo_residuo": "general",
    "nivel_urgencia": "alto",
    "estado": "nuevo",
    "imagen_url": "https://...",
    "fecha_creacion": "2026-05-05T10:30:00",
    "usuario_nombre": "Juan Rodríguez"
  },
  ...
]
```

---

### Obtener un Reporte Específico

**GET** `/reportes/<id>`

Obtiene un reporte por ID.

**Response (200):**
```json
{
  "id": 1,
  "usuario_id": 1,
  "titulo": "Acumulación de residuos en Bazurto",
  "descripcion": "Hay una gran cantidad de residuos...",
  "ubicacion": "Bazurto, Cartagena",
  "latitud": 10.3932,
  "longitud": -75.5136,
  "tipo_residuo": "general",
  "nivel_urgencia": "alto",
  "estado": "nuevo",
  "imagen_url": "https://...",
  "fecha_creacion": "2026-05-05T10:30:00",
  "usuario_nombre": "Juan Rodríguez"
}
```

---

### Crear Nuevo Reporte

**POST** `/reportes`

Crea un nuevo reporte de residuos.

**Request:**
```json
{
  "usuario_id": 1,
  "titulo": "Residuos en la calle principal",
  "descripcion": "Se han acumulado bolsas de basura...",
  "ubicacion": "Calle 10, Cartagena",
  "latitud": 10.3920,
  "longitud": -75.5125,
  "tipo_residuo": "general",
  "nivel_urgencia": "medio",
  "imagen_url": ""
}
```

**Response (201):**
```json
{
  "success": true,
  "reporte_id": 7
}
```

---

### Actualizar Reporte

**PUT** `/reportes/<id>`

Actualiza el estado de un reporte.

**Request:**
```json
{
  "estado": "en_proceso"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Reporte actualizado"
}
```

**Estados válidos:**
- `nuevo` - Recién creado
- `en_proceso` - En atención
- `resuelto` - Completado

---

## 🚚 Rutas de Recolección

### Obtener Todas las Rutas

**GET** `/rutas`

Obtiene todas las rutas de recolección.

**Response (200):**
```json
[
  {
    "id": 1,
    "operador_id": 3,
    "estado": "en_proceso",
    "fecha_asignacion": "2026-05-05T08:00:00",
    "hora_estimada": "08:00",
    "zonas_cobertura": "Bazurto - Centro",
    "ubicacion_inicio": "Carrera 1",
    "ubicacion_fin": "Carrera 10",
    "fecha_finalizacion": "2026-05-05T12:00:00",
    "operador_nombre": "Carlos López"
  },
  ...
]
```

---

### Crear Nueva Ruta

**POST** `/rutas`

Crea una nueva ruta de recolección.

**Request:**
```json
{
  "operador_id": 3,
  "hora_estimada": "10:00",
  "zonas_cobertura": "San Diego - Getsemaní",
  "ubicacion_inicio": "Carrera 5",
  "ubicacion_fin": "Carrera 15"
}
```

**Response (201):**
```json
{
  "success": true,
  "ruta_id": 5
}
```

---

## 🔔 Alertas

### Obtener Todas las Alertas

**GET** `/alertas`

Obtiene las últimas 50 alertas del sistema.

**Response (200):**
```json
[
  {
    "id": 1,
    "reporte_id": 1,
    "mensaje": "Nuevo reporte: Acumulación de residuos en Bazurto",
    "tipo_alerta": "reporte_nuevo",
    "estado": "activa",
    "fecha_creacion": "2026-05-05T10:30:00",
    "fecha_lectura": null
  },
  ...
]
```

---

### Obtener Alertas de un Usuario

**GET** `/alertas/usuario/<id>`

Obtiene las alertas relacionadas con un usuario específico.

**Response (200):**
```json
[
  {
    "id": 1,
    "reporte_id": 1,
    "mensaje": "Tu reporte: Acumulación de residuos...",
    "tipo_alerta": "reporte_nuevo",
    "estado": "activa",
    "fecha_creacion": "2026-05-05T10:30:00",
    "fecha_lectura": null
  },
  ...
]
```

---

## 📊 Estadísticas

### Obtener Estadísticas Generales

**GET** `/estadisticas`

Obtiene estadísticas generales del sistema.

**Response (200):**
```json
{
  "total_reportes": 6,
  "reportes_resueltos": 1,
  "reportes_pendientes": 5,
  "total_usuarios": 8,
  "por_tipo_residuo": [
    {
      "tipo_residuo": "general",
      "cantidad": 4
    },
    {
      "tipo_residuo": "peligroso",
      "cantidad": 1
    },
    {
      "tipo_residuo": "plástico",
      "cantidad": 1
    }
  ],
  "por_urgencia": [
    {
      "nivel_urgencia": "alto",
      "cantidad": 2
    },
    {
      "nivel_urgencia": "medio",
      "cantidad": 3
    },
    {
      "nivel_urgencia": "crítico",
      "cantidad": 1
    }
  ]
}
```

---

## 👥 Usuarios

### Obtener Todos los Usuarios

**GET** `/usuarios`

Obtiene la lista de todos los usuarios (requiere ser admin).

**Response (200):**
```json
[
  {
    "id": 1,
    "nombre": "Juan Rodríguez",
    "email": "juan@example.com",
    "rol": "ciudadano",
    "telefono": "3001234567",
    "estado": "activo"
  },
  ...
]
```

---

### Obtener Perfil de Usuario

**GET** `/usuarios/<id>`

Obtiene el perfil de un usuario específico.

**Response (200):**
```json
{
  "id": 1,
  "nombre": "Juan Rodríguez",
  "email": "juan@example.com",
  "rol": "ciudadano",
  "telefono": "3001234567",
  "imagen_perfil": "https://...",
  "estado": "activo"
}
```

---

## ✅ Health Check

### Verificar Estado del Servidor

**GET** `/health`

Verifica que el servidor está corriendo.

**Response (200):**
```json
{
  "status": "ok",
  "message": "Servidor de residuos-cartagena activo"
}
```

---

## 📋 Enumeraciones

### Estados de Reporte
- `nuevo` - Recién reportado
- `en_proceso` - Siendo atendido
- `resuelto` - Completado

### Tipo de Residuo
- `general` - Residuos generales
- `plástico` - Plásticos
- `orgánico` - Residuos orgánicos
- `peligroso` - Residuos peligrosos

### Nivel de Urgencia
- `bajo` - Baja urgencia
- `medio` - Urgencia media
- `alto` - Alta urgencia
- `crítico` - Crítica/Emergencia

### Roles de Usuario
- `ciudadano` - Ciudadano (reporta problemas)
- `operador` - Operador de aseo (recoge residuos)
- `admin` - Administrador (gestiona el sistema)

### Estados de Ruta
- `asignada` - Ruta asignada
- `en_proceso` - En ejecución
- `completada` - Finalizada

---

## 🔒 Códigos de Estado HTTP

| Código | Significado |
|--------|------------|
| 200 | OK - Solicitud exitosa |
| 201 | Created - Recurso creado |
| 400 | Bad Request - Solicitud inválida |
| 401 | Unauthorized - No autenticado |
| 404 | Not Found - Recurso no encontrado |
| 500 | Internal Server Error - Error del servidor |

---

## 💡 Ejemplos de Uso

### Con cURL

```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"juan@example.com","password":"pass123"}'

# Obtener reportes
curl http://localhost:5000/api/reportes

# Crear reporte
curl -X POST http://localhost:5000/api/reportes \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": 1,
    "titulo": "Residuos en la calle",
    "descripcion": "Bolsas de basura acumuladas",
    "ubicacion": "Calle 10",
    "latitud": 10.3920,
    "longitud": -75.5125,
    "tipo_residuo": "general",
    "nivel_urgencia": "medio"
  }'
```

### Con Python

```python
import requests

# Login
response = requests.post('http://localhost:5000/api/auth/login', json={
    'email': 'juan@example.com',
    'password': 'pass123'
})
user_data = response.json()

# Obtener reportes
response = requests.get('http://localhost:5000/api/reportes')
reportes = response.json()

# Crear reporte
response = requests.post('http://localhost:5000/api/reportes', json={
    'usuario_id': 1,
    'titulo': 'Residuos acumulados',
    'descripcion': 'Hay basura en la calle',
    'ubicacion': 'Centro, Cartagena',
    'latitud': 10.3920,
    'longitud': -75.5125,
    'tipo_residuo': 'general',
    'nivel_urgencia': 'medio'
})
```

---

**Última actualización: Mayo 2026**
