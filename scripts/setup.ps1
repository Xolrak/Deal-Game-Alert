$raiz = Join-Path $PSScriptRoot ".."

Write-Host "Creando entorno virtual..." -ForegroundColor Cyan
python -m venv "$raiz\venv"

Write-Host "Actualizando pip..." -ForegroundColor Cyan
& "$raiz\venv\Scripts\python.exe" -m pip install --upgrade pip

Write-Host "Instalando dependencias desde requirements.txt..." -ForegroundColor Cyan
& "$raiz\venv\Scripts\python.exe" -m pip install -r "$raiz\requirements.txt"

Write-Host "Entorno preparado con éxito." -ForegroundColor Green