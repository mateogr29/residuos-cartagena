-- ==================== TABLA USUARIOS ====================
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL DEFAULT 'ciudadano',
    telefono TEXT,
    imagen_perfil TEXT,
    estado TEXT DEFAULT 'activo',
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME
);

-- ==================== TABLA REPORTES ====================
CREATE TABLE IF NOT EXISTS reportes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    ubicacion TEXT NOT NULL,
    latitud REAL,
    longitud REAL,
    tipo_residuo TEXT DEFAULT 'general',
    nivel_urgencia TEXT DEFAULT 'medio',
    estado TEXT DEFAULT 'nuevo',
    imagen_url TEXT,
    fecha_creacion DATETIME,
    fecha_actualizacion DATETIME,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- ==================== TABLA RUTAS DE RECOLECCIÓN ====================
CREATE TABLE IF NOT EXISTS rutas_recoleccion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operador_id INTEGER,
    estado TEXT DEFAULT 'asignada',
    fecha_asignacion DATETIME,
    hora_estimada TEXT,
    zonas_cobertura TEXT,
    ubicacion_inicio TEXT,
    ubicacion_fin TEXT,
    fecha_finalizacion DATETIME,
    FOREIGN KEY (operador_id) REFERENCES usuarios(id)
);

-- ==================== TABLA ALERTAS ====================
CREATE TABLE IF NOT EXISTS alertas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reporte_id INTEGER,
    mensaje TEXT NOT NULL,
    tipo_alerta TEXT DEFAULT 'reporte_nuevo',
    estado TEXT DEFAULT 'activa',
    fecha_creacion DATETIME,
    fecha_lectura DATETIME,
    FOREIGN KEY (reporte_id) REFERENCES reportes(id)
);

-- ==================== TABLA SUSCRIPCIONES ====================
CREATE TABLE IF NOT EXISTS suscripciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    alerta_id INTEGER NOT NULL,
    tipo_notificacion TEXT DEFAULT 'push',
    estado TEXT DEFAULT 'activa',
    fecha_suscripcion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (alerta_id) REFERENCES alertas(id)
);

-- ==================== TABLA ASIGNACIONES ====================
CREATE TABLE IF NOT EXISTS asignaciones_recoleccion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ruta_id INTEGER NOT NULL,
    reporte_id INTEGER NOT NULL,
    operador_id INTEGER NOT NULL,
    estado TEXT DEFAULT 'asignado',
    fecha_asignacion DATETIME,
    fecha_confirmacion DATETIME,
    FOREIGN KEY (ruta_id) REFERENCES rutas_recoleccion(id),
    FOREIGN KEY (reporte_id) REFERENCES reportes(id),
    FOREIGN KEY (operador_id) REFERENCES usuarios(id)
);

-- ==================== ÍNDICES ====================
CREATE INDEX IF NOT EXISTS idx_reportes_usuario ON reportes(usuario_id);
CREATE INDEX IF NOT EXISTS idx_reportes_estado ON reportes(estado);
CREATE INDEX IF NOT EXISTS idx_rutas_operador ON rutas_recoleccion(operador_id);
CREATE INDEX IF NOT EXISTS idx_alertas_reporte ON alertas(reporte_id);
