#!/bin/bash

# Colores para la terminal
CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color / Restablecer

DIR_SCRIPT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
RAIZ="$DIR_SCRIPT/.."

echo -e "${CYAN}Creando entorno virtual...${NC}"
python3 -m venv "$RAIZ/venv"

echo -e "${CYAN}Actualizando pip...${NC}"
"$RAIZ/venv/bin/python" -m pip install --upgrade pip

echo -e "${CYAN}Instalando dependencias desde requirements.txt...${NC}"
"$RAIZ/venv/bin/python" -m pip install -r "$RAIZ/requirements.txt"

echo -e "${GREEN}Entorno preparado con éxito.${NC}"