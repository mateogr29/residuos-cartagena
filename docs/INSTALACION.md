# 🔧 Guía de Instalación - Plataforma de Residuos

Sigue los pasos a continuación para instalar y ejecutar la plataforma completa.

## 📋 Requisitos Previos

### Windows/Mac/Linux

- **Python 3.8 o superior**
  - Descarga desde: https://www.python.org/downloads/
  - ✅ Marca "Add Python to PATH" (Windows)

- **Flutter SDK**
  - Descarga desde: https://flutter.dev/docs/get-started/install
  - Versión recomendada: 3.0+

- **Git** (opcional)
  - Para clonar repositorios

- **Visual Studio Code** (recomendado)
  - Descarga desde: https://code.visualstudio.com/

## 🚀 Instalación del Backend

### Paso 1: Abre PowerShell o Terminal

Navega a la carpeta `backend`:

```powershell
cd C:\Users\[TuUsuario]\Downloads\residuos-cartagena\backend
```

### Paso 2: Crea un Entorno Virtual

```powershell
python -m venv venv
```

### Paso 3: Activa el Entorno Virtual

**En Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**En Mac/Linux:**
```bash
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### Paso 4: Instala las Dependencias

```powershell
pip install -r requirements.txt
```

Espera a que se instalen todos los paquetes.

### Paso 5: Ejecuta el Servidor

```powershell
python app.py
```

Si todo está correcto, verás:

```
✓ Base de datos inicializada
 * Running on http://0.0.0.0:5000
```

**El servidor está activo en:** `http://localhost:5000`

### Verificar que Funciona

Abre tu navegador y ve a:
```
http://localhost:5000/api/health
```

Deberías ver:
```json
{
  "status": "ok",
  "message": "Servidor de residuos-cartagena activo"
}
```

## 📱 Instalación del Frontend (Flutter)

### Paso 1: Verifica que Flutter está Instalado

Abre una nueva terminal y ejecuta:

```powershell
flutter --version
```

Si no está instalado, descárgalo de: https://flutter.dev/docs/get-started/install

### Paso 2: Obtén Dependencias de Flutter

Navega a la carpeta frontend:

```powershell
cd C:\Users\[TuUsuario]\Downloads\residuos-cartagena\frontend
```

Ejecuta:

```powershell
flutter pub get
```

### Paso 3: Configura la URL de la API

**Importante:** Necesitas la IP local de tu computadora.

#### Encuentra tu IP Local

**En Windows (PowerShell):**
```powershell
ipconfig
```

Busca la línea que dice "Dirección IPv4" bajo tu conexión de red activa. Será algo como:
```
Dirección IPv4 . . . . . . . . . : 192.168.1.100
```

**En Mac/Linux:**
```bash
ifconfig
```

Busca "inet" (sin "inet6"). Algo como: `192.168.1.100`

#### Edita el Archivo api_service.dart

1. Abre: `frontend/lib/services/api_service.dart`
2. Busca la línea:
   ```dart
   static const String baseUrl = 'http://192.168.1.100:5000/api';
   ```
3. Reemplaza `192.168.1.100` con tu IP local
4. Guarda el archivo

### Paso 4: Ejecuta la Aplicación

#### Opción A: En Dispositivo Físico Android

1. Conecta tu teléfono por USB
2. Activa "Depuración por USB" en el teléfono
3. Ejecuta:
   ```powershell
   flutter run
   ```

#### Opción B: En Emulador Android

1. Abre Android Studio
2. Abre AVD Manager
3. Inicia un emulador
4. Ejecuta:
   ```powershell
   flutter run
   ```

#### Opción C: En Desktop (Windows/Mac/Linux)

```powershell
flutter run -d windows
# o
flutter run -d macos
# o
flutter run -d linux
```

## 🧪 Pruebas Iniciales

### Datos de Acceso

**Usuario 1 (Ciudadano):**
```
Email: juan@example.com
Contraseña: pass123
```

**Usuario 2 (Ciudadano):**
```
Email: maria@example.com
Contraseña: pass123
```

**Usuario 3 (Operador):**
```
Email: carlos@example.com
Contraseña: pass123
```

**Usuario 4 (Administrador):**
```
Email: admin@example.com
Contraseña: admin123
```

### Pasos de Prueba

1. **Inicia Sesión**: Usa juan@example.com / pass123
2. **Ver Dashboard**: Observa los reportes y estadísticas
3. **Ver Reportes**: Navega a la sección de reportes
4. **Ver Rutas**: Verifica las rutas de recolección
5. **Ver Alertas**: Revisa las alertas del sistema
6. **Ver Perfil**: Accede a tu información de usuario

## 🐳 Instalación con Docker (Opcional)

Si tienes Docker instalado, puedes ejecutar todo en contenedores:

### Paso 1: Crea un archivo docker-compose.yml

Ubicación: `residuos-cartagena/docker-compose.yml`

```yaml
version: '3.8'

services:
  api:
    build:
      context: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - FLASK_DEBUG=True
    volumes:
      - ./database:/app/database
    command: python app.py
```

### Paso 2: Ejecuta

```powershell
docker-compose up --build
```

## ❌ Solución de Problemas

### Error: "Port 5000 already in use"

Hay otra aplicación usando el puerto 5000.

**Solución:**
```powershell
# Encuentra qué usa el puerto 5000
netstat -ano | findstr :5000

# Mata el proceso (reemplaza PID)
taskkill /PID <PID> /F
```

### Error: "ModuleNotFoundError: No module named 'flask'"

No instalaste las dependencias.

**Solución:**
```powershell
# Asegúrate que el entorno virtual está activo
pip install -r requirements.txt
```

### Error: "ConnectionRefused" en la app

La app no puede conectar con el servidor.

**Soluciones:**
1. Verifica que el servidor está corriendo: `http://localhost:5000/api/health`
2. Verifica que la IP en `api_service.dart` es correcta
3. Desactiva el firewall temporalmente para probar

### Error: "Flutter not found"

Flutter no está instalado o no está en PATH.

**Solución:**
1. Descarga Flutter: https://flutter.dev/docs/get-started/install
2. Agrega Flutter a tu PATH

### Error: "No connected devices"

No hay dispositivo conectado para ejecutar la app.

**Soluciones:**
1. Conecta un dispositivo Android por USB
2. O usa un emulador
3. Ejecuta: `flutter devices` para ver dispositivos disponibles

## 📚 Próximos Pasos

1. Familiarízate con la estructura del código
2. Personaliza la configuración según tus necesidades
3. Agrega más reportes de prueba
4. Prueba los diferentes roles (ciudadano, operador, admin)
5. Explora la documentación de la API en [API.md](API.md)

## 🆘 Necesitas Ayuda?

- Lee la sección de Solución de Problemas
- Revisa los logs en la terminal del servidor
- Verifica que todas las dependencias están instaladas

---

**¡Felicidades! Ahora deberías tener el proyecto corriendo completo.** 🎉
