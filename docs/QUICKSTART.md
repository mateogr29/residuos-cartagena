# ⚡ Inicio Rápido (5 minutos)

¡Inicia la plataforma en 5 minutos! Sigue estos pasos.

## 1️⃣ Backend (Python)

Abre PowerShell y ejecuta:

```powershell
cd C:\Users\[TuUsuario]\Downloads\residuos-cartagena\backend

python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

**Espera a ver**: `Running on http://0.0.0.0:5000`

✅ Backend está corriendo.

---

## 2️⃣ Frontend (Flutter)

Abre otra terminal PowerShell y ejecuta:

```powershell
cd C:\Users\[TuUsuario]\Downloads\residuos-cartagena\frontend

flutter pub get
flutter run
```

**Selecciona tu dispositivo** cuando pregunte.

✅ App está corriendo.

---

## 3️⃣ Login

En la app, usa:

```
Email: juan@example.com
Contraseña: pass123
```

✅ ¡Listo! Estás dentro.

---

## 📱 Qué Hacer Ahora

1. **Explorar**: Navega por las diferentes pantallas
2. **Reportar**: Crea un nuevo reporte de residuos
3. **Ver Estadísticas**: Revisa el dashboard
4. **Cambiar de Usuario**: Logout y prueba otro rol

---

## ⚠️ Si Algo No Funciona

### Error de Conexión

```
❌ "Failed to connect to server"
```

**Solución:**

1. Busca tu IP local:
   ```powershell
   ipconfig
   ```
   
2. Edita: `frontend/lib/services/api_service.dart`

3. Reemplaza en esta línea:
   ```dart
   static const String baseUrl = 'http://192.168.1.100:5000/api';
   ```
   
   Con tu IP (ej: `192.168.1.50`)

4. Reinicia la app: `flutter run`

---

### Puerto ya Está Siendo Usado

```
❌ "Port 5000 already in use"
```

**Solución:**

```powershell
netstat -ano | findstr :5000
taskkill /PID [PID] /F
python app.py
```

---

### Flutter No Encontrado

```
❌ "flutter: command not found"
```

**Solución:**

Descarga Flutter desde: https://flutter.dev/docs/get-started/install

---

## 🎯 Próximos Pasos

- Lee [INSTALACION.md](INSTALACION.md) para una guía completa
- Revisa [API.md](API.md) para documentación de endpoints
- Explorat el código en `frontend/lib/` y `backend/`

---

**¡Disfruta explorando la plataforma!** 🚀
