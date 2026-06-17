-- ==================== DATOS DE EJEMPLO - USUARIOS ====================

INSERT INTO usuarios (nombre, email, password, rol, telefono, imagen_perfil, estado) VALUES
('Juan Rodríguez', 'juan@example.com', 'pass123', 'ciudadano', '3001234567', 'https://via.placeholder.com/150', 'activo'),
('María García', 'maria@example.com', 'pass123', 'ciudadano', '3001234568', 'https://via.placeholder.com/150', 'activo'),
('Carlos López', 'carlos@example.com', 'pass123', 'operador', '3001234569', 'https://via.placeholder.com/150', 'activo'),
('Sandra Martínez', 'sandra@example.com', 'pass123', 'operador', '3001234570', 'https://via.placeholder.com/150', 'activo'),
('Admin Sistema', 'admin@example.com', 'admin123', 'admin', '3001234571', 'https://via.placeholder.com/150', 'activo'),
('Pedro Jiménez', 'pedro@example.com', 'pass123', 'ciudadano', '3001234572', 'https://via.placeholder.com/150', 'activo'),
('Laura Espinosa', 'laura@example.com', 'pass123', 'ciudadano', '3001234573', 'https://via.placeholder.com/150', 'activo'),
('Roberto Díaz', 'roberto@example.com', 'pass123', 'operador', '3001234574', 'https://via.placeholder.com/150', 'activo');

-- ==================== DATOS DE EJEMPLO - REPORTES ====================

INSERT INTO reportes (usuario_id, titulo, descripcion, ubicacion, latitud, longitud, tipo_residuo, nivel_urgencia, estado, imagen_url, fecha_creacion) VALUES
(1, 'Acumulación de residuos en Bazurto', 'Hay una gran cantidad de residuos acumulados en la calle principal', 'Bazurto, Cartagena', 10.3932, -75.5136, 'general', 'alto', 'nuevo', 'https://via.placeholder.com/300', datetime('now')),
(2, 'Bolsas de basura en el piso', 'Se han derramado varias bolsas de basura en la esquina de la calle', 'Centro, Cartagena', 10.3910, -75.5150, 'general', 'medio', 'en_proceso', 'https://via.placeholder.com/300', datetime('now', '-1 day')),
(1, 'Residuos peligrosos detectados', 'Hay material que parece ser peligroso tirado en la calle', 'Bazurto, Cartagena', 10.3945, -75.5120, 'peligroso', 'crítico', 'nuevo', 'https://via.placeholder.com/300', datetime('now', '-2 hours')),
(6, 'Mala disposición de residuos plásticos', 'Cantidad excesiva de plásticos acumulados en un punto específico', 'San Diego, Cartagena', 10.4013, -75.5150, 'plástico', 'medio', 'resuelto', 'https://via.placeholder.com/300', datetime('now', '-3 days')),
(7, 'Residuos orgánicos en descomposición', 'Se percibe mal olor por acumulación de residuos orgánicos', 'Getsemaní, Cartagena', 10.3854, -75.5254, 'orgánico', 'alto', 'en_proceso', 'https://via.placeholder.com/300', datetime('now', '-12 hours')),
(1, 'Contenedores desbordados', 'Los contenedores de basura están llenos y hay residuos alrededor', 'Bazurto, Cartagena', 10.3920, -75.5125, 'general', 'medio', 'nuevo', 'https://via.placeholder.com/300', datetime('now', '-30 minutes'));

-- ==================== DATOS DE EJEMPLO - RUTAS DE RECOLECCIÓN ====================

INSERT INTO rutas_recoleccion (operador_id, estado, fecha_asignacion, hora_estimada, zonas_cobertura, ubicacion_inicio, ubicacion_fin, lat_inicio, lng_inicio, lat_fin, lng_fin, fecha_finalizacion) VALUES
(3, 'en_proceso', datetime('now'), '08:00', 'Bazurto - Centro', 'Carrera 1', 'Carrera 10', 10.3920, -75.5125, 10.4236, -75.5478, datetime('now', '+4 hours')),
(3, 'asignada', datetime('now'), '10:00', 'San Diego - Getsemaní', 'Carrera 5', 'Carrera 15', 10.4231, -75.5497, 10.3854, -75.5254, datetime('now', '+6 hours')),
(4, 'completada', datetime('now', '-1 day'), '07:00', 'Centro - Bazurto', 'Carrera 2', 'Carrera 8', 10.4236, -75.5478, 10.3920, -75.5125, datetime('now', '-1 day', '+4 hours')),
(8, 'asignada', datetime('now'), '14:00', 'Pedregal - Arborizadora', 'Carrera 20', 'Carrera 30', 10.3717, -75.4889, 10.3650, -75.4810, datetime('now', '+6 hours'));

-- ==================== DATOS DE EJEMPLO - ALERTAS ====================

INSERT INTO alertas (reporte_id, mensaje, tipo_alerta, estado, fecha_creacion) VALUES
(1, 'Nuevo reporte: Acumulación de residuos en Bazurto', 'reporte_nuevo', 'activa', datetime('now')),
(2, 'Reporte en proceso: Bolsas de basura en el piso', 'reporte_en_proceso', 'activa', datetime('now', '-1 day')),
(3, 'ALERTA CRÍTICA: Residuos peligrosos detectados', 'reporte_critico', 'activa', datetime('now', '-2 hours')),
(5, 'Reporte en atención: Residuos orgánicos en descomposición', 'reporte_en_proceso', 'activa', datetime('now', '-12 hours')),
(6, 'Nuevo reporte: Contenedores desbordados', 'reporte_nuevo', 'activa', datetime('now', '-30 minutes'));

-- ==================== DATOS DE EJEMPLO - SUSCRIPCIONES ====================

INSERT INTO suscripciones (usuario_id, alerta_id, tipo_notificacion, estado) VALUES
(1, 1, 'push', 'activa'),
(2, 2, 'push', 'activa'),
(3, 3, 'push', 'activa'),
(6, 4, 'push', 'activa'),
(7, 5, 'push', 'activa');

-- ==================== DATOS DE EJEMPLO - ASIGNACIONES ====================

INSERT INTO asignaciones_recoleccion (ruta_id, reporte_id, operador_id, estado, fecha_asignacion) VALUES
(1, 1, 3, 'en_proceso', datetime('now')),
(1, 6, 3, 'asignado', datetime('now')),
(2, 5, 4, 'asignado', datetime('now')),
(4, 3, 8, 'asignado', datetime('now'));
