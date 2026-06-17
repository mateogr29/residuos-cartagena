from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuración de base de datos
DATABASE = os.path.join(os.path.dirname(__file__), '..', 'database', 'residuos.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializar base de datos si no existe"""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Crear tablas
        with open(os.path.join(os.path.dirname(__file__), '..', 'database', 'schema.sql'), encoding='utf-8') as f:
            cursor.executescript(f.read())
        
        # Insertar datos de ejemplo
        with open(os.path.join(os.path.dirname(__file__), '..', 'database', 'data_ejemplo.sql'), encoding='utf-8') as f:
            cursor.executescript(f.read())
        
        conn.commit()
        conn.close()

# ==================== RUTAS DE AUTENTICACIÓN ====================

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login de usuario"""
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM usuarios WHERE email = ? AND password = ?', (email, password)).fetchone()
    conn.close()
    
    if user:
        return jsonify({
            'success': True,
            'user': {
                'id': user['id'],
                'nombre': user['nombre'],
                'email': user['email'],
                'rol': user['rol'],
                'imagen_perfil': user['imagen_perfil']
            }
        }), 200
    
    return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 401

@app.route('/api/auth/register', methods=['POST'])
def register():
    """Registrar nuevo usuario"""
    data = request.json
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nombre, email, password, rol, telefono, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data['nombre'], data['email'], data['password'], 'ciudadano', data.get('telefono', ''), 'activo'))
        conn.commit()
        
        user_id = cursor.lastrowid
        return jsonify({
            'success': True,
            'message': 'Usuario registrado exitosamente',
            'user_id': user_id
        }), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
    finally:
        conn.close()

# ==================== RUTAS DE REPORTES ====================

@app.route('/api/reportes', methods=['GET'])
def get_reportes():
    """Obtener todos los reportes"""
    conn = get_db_connection()
    reportes = conn.execute('''
        SELECT r.*, u.nombre as usuario_nombre, u.imagen_perfil 
        FROM reportes r
        JOIN usuarios u ON r.usuario_id = u.id
        ORDER BY r.fecha_creacion DESC
    ''').fetchall()
    conn.close()
    
    return jsonify([dict(r) for r in reportes]), 200

@app.route('/api/reportes/<int:id>', methods=['GET'])
def get_reporte(id):
    """Obtener un reporte específico"""
    conn = get_db_connection()
    reporte = conn.execute('''
        SELECT r.*, u.nombre as usuario_nombre 
        FROM reportes r
        JOIN usuarios u ON r.usuario_id = u.id
        WHERE r.id = ?
    ''', (id,)).fetchone()
    conn.close()
    
    if reporte:
        return jsonify(dict(reporte)), 200
    return jsonify({'message': 'Reporte no encontrado'}), 404

@app.route('/api/reportes', methods=['POST'])
def crear_reporte():
    """Crear nuevo reporte de residuos"""
    data = request.json
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reportes (usuario_id, titulo, descripcion, ubicacion, latitud, longitud, 
                                tipo_residuo, nivel_urgencia, estado, imagen_url, fecha_creacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['usuario_id'],
            data['titulo'],
            data['descripcion'],
            data['ubicacion'],
            data['latitud'],
            data['longitud'],
            data.get('tipo_residuo', 'general'),
            data.get('nivel_urgencia', 'medio'),
            'nuevo',
            data.get('imagen_url', ''),
            datetime.now().isoformat()
        ))
        conn.commit()
        reporte_id = cursor.lastrowid
        
        # Crear alerta automática
        cursor.execute('''
            INSERT INTO alertas (reporte_id, mensaje, tipo_alerta, estado, fecha_creacion)
            VALUES (?, ?, ?, ?, ?)
        ''', (reporte_id, f"Nuevo reporte: {data['titulo']}", 'reporte_nuevo', 'activa', datetime.now().isoformat()))
        
        conn.commit()
        return jsonify({'success': True, 'reporte_id': reporte_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
    finally:
        conn.close()

@app.route('/api/reportes/<int:id>', methods=['PUT'])
def actualizar_reporte(id):
    """Actualizar estado de reporte"""
    data = request.json
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE reportes 
            SET estado = ?, fecha_actualizacion = ?
            WHERE id = ?
        ''', (data['estado'], datetime.now().isoformat(), id))
        conn.commit()
        return jsonify({'success': True, 'message': 'Reporte actualizado'}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
    finally:
        conn.close()

# ==================== RUTAS DE RUTAS DE RECOLECCIÓN ====================

@app.route('/api/rutas', methods=['GET'])
def get_rutas():
    """Obtener todas las rutas de recolección"""
    conn = get_db_connection()
    rutas = conn.execute('''
        SELECT r.*, op.nombre as operador_nombre
        FROM rutas_recoleccion r
        LEFT JOIN usuarios op ON r.operador_id = op.id
        ORDER BY r.fecha_asignacion DESC
    ''').fetchall()
    conn.close()
    
    return jsonify([dict(r) for r in rutas]), 200

@app.route('/api/rutas', methods=['POST'])
def crear_ruta():
    """Crear nueva ruta de recolección"""
    data = request.json
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO rutas_recoleccion (operador_id, estado, fecha_asignacion, hora_estimada, 
                                         zonas_cobertura, ubicacion_inicio, ubicacion_fin)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['operador_id'],
            'asignada',
            datetime.now().isoformat(),
            data.get('hora_estimada', '08:00'),
            data.get('zonas_cobertura', 'Centro'),
            data.get('ubicacion_inicio', ''),
            data.get('ubicacion_fin', '')
        ))
        conn.commit()
        ruta_id = cursor.lastrowid
        return jsonify({'success': True, 'ruta_id': ruta_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
    finally:
        conn.close()

# ==================== RUTAS DE ALERTAS ====================

@app.route('/api/alertas', methods=['GET'])
def get_alertas():
    """Obtener todas las alertas"""
    conn = get_db_connection()
    alertas = conn.execute('SELECT * FROM alertas ORDER BY fecha_creacion DESC LIMIT 50').fetchall()
    conn.close()
    
    return jsonify([dict(a) for a in alertas]), 200

@app.route('/api/alertas/usuario/<int:usuario_id>', methods=['GET'])
def get_alertas_usuario(usuario_id):
    """Obtener alertas de un usuario específico"""
    conn = get_db_connection()
    alertas = conn.execute('''
        SELECT * FROM alertas 
        WHERE reporte_id IN (SELECT id FROM reportes WHERE usuario_id = ?)
        OR ? IN (SELECT usuario_id FROM suscripciones WHERE alerta_id = alertas.id)
        ORDER BY fecha_creacion DESC
    ''', (usuario_id, usuario_id)).fetchall()
    conn.close()
    
    return jsonify([dict(a) for a in alertas]), 200

# ==================== RUTAS DE ESTADÍSTICAS ====================

@app.route('/api/estadisticas', methods=['GET'])
def get_estadisticas():
    """Obtener estadísticas generales del sistema"""
    conn = get_db_connection()
    
    total_reportes = conn.execute('SELECT COUNT(*) as count FROM reportes').fetchone()['count']
    reportes_resueltos = conn.execute("SELECT COUNT(*) as count FROM reportes WHERE estado='resuelto'").fetchone()['count']
    reportes_pendientes = conn.execute("SELECT COUNT(*) as count FROM reportes WHERE estado IN ('nuevo', 'en_proceso')").fetchone()['count']
    total_usuarios = conn.execute('SELECT COUNT(*) as count FROM usuarios').fetchone()['count']
    
    por_tipo_residuo = conn.execute('''
        SELECT tipo_residuo, COUNT(*) as cantidad 
        FROM reportes 
        GROUP BY tipo_residuo
    ''').fetchall()
    
    por_urgencia = conn.execute('''
        SELECT nivel_urgencia, COUNT(*) as cantidad 
        FROM reportes 
        GROUP BY nivel_urgencia
    ''').fetchall()
    
    conn.close()
    
    return jsonify({
        'total_reportes': total_reportes,
        'reportes_resueltos': reportes_resueltos,
        'reportes_pendientes': reportes_pendientes,
        'total_usuarios': total_usuarios,
        'por_tipo_residuo': [dict(r) for r in por_tipo_residuo],
        'por_urgencia': [dict(r) for r in por_urgencia]
    }), 200

# ==================== RUTAS DE USUARIOS ====================

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    """Obtener todos los usuarios (solo para admins)"""
    conn = get_db_connection()
    usuarios = conn.execute('SELECT id, nombre, email, rol, telefono, estado FROM usuarios').fetchall()
    conn.close()
    
    return jsonify([dict(u) for u in usuarios]), 200

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    """Obtener perfil de usuario"""
    conn = get_db_connection()
    usuario = conn.execute('SELECT id, nombre, email, rol, telefono, imagen_perfil, estado FROM usuarios WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if usuario:
        return jsonify(dict(usuario)), 200
    return jsonify({'message': 'Usuario no encontrado'}), 404

# ==================== RUTA RAÍZ ====================

@app.route('/', methods=['GET'])
def index():
    """Ruta raíz del servidor"""
    return jsonify({
        'status': 'ok',
        'message': 'Servidor de residuos-cartagena activo',
        'endpoints': {
            'health': '/api/health',
            'auth': {
                'login': 'POST /api/auth/login',
                'register': 'POST /api/auth/register'
            },
            'reportes': {
                'get_all': 'GET /api/reportes',
                'get_one': 'GET /api/reportes/<id>',
                'create': 'POST /api/reportes',
                'update': 'PUT /api/reportes/<id>'
            },
            'rutas': {
                'get_all': 'GET /api/rutas',
                'create': 'POST /api/rutas'
            },
            'alertas': {
                'get_all': 'GET /api/alertas',
                'get_user': 'GET /api/alertas/usuario/<id>'
            },
            'estadisticas': 'GET /api/estadisticas',
            'usuarios': {
                'get_all': 'GET /api/usuarios',
                'get_one': 'GET /api/usuarios/<id>'
            }
        }
    }), 200

# ==================== RUTA DE PRUEBA ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Verificar que el servidor está funcionando"""
    return jsonify({'status': 'ok', 'message': 'Servidor de residuos-cartagena activo'}), 200

# ==================== INICIALIZACIÓN ====================

init_db()
print("✓ Base de datos inicializada")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
