# 🎮 DealGameAlert

Bot modular que rastrea ofertas de juegos 100% gratuitos a través de la API de CheapShark y envía notificaciones por Discord de manera automática mediante Webhooks.

## 🚀 Características
* **Rastreo de ofertas:** Consulta la API de CheapShark buscando los juegos gratuitos.
* **Notificaciones por Discord:** Envíos con el título, imagen y enlaces directos.
* **Registro local:** Se guarda un histórico de las ofertas ya enviadas para evitar el spam.
* **Seguridad:** Configuración segura usando archivos de configuración apartados del código

## 🛠️ Instalación
1. **Clonación del repositorio**
```bash
git clone https://github.com/Xolrak/DealGameAlert.git
cd DealGameAlert
```

2. **Preparación del entorno**
```bash
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. **Crear variables de entorno**
```bash
cp .env.example .env
```
Aqui se debe añadir la URL del Webhook

4. **Ejecutar bot**
- Windows
```powershell
.\venv\Scripts\python.exe main.py
```
- Linux
```bash
./venv/bin/python main.py
```