Write-Host "Creando entorno virtual..." -ForegroundColor Cyan
python -m venv venv

Write-Host "Actualizando pip..." -ForegroundColor Cyan
.\venv\Scripts\python.exe -m pip install --upgrade pip

Write-Host "Instalando dependencias desde requirements.txt..." -ForegroundColor Cyan
.\venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host "Entorno preparado con éxito." -ForegroundColor Green