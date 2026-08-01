# config.py
import os
from dotenv import load_dotenv

load_dotenv()

## CONSTANTES
URL_DESCUENTOS = "https://www.cheapshark.com/api/1.0/deals"
URL_TIENDAS = "https://www.cheapshark.com/api/1.0/stores"
WEBHOOK_DISCORD = os.getenv("WEBHOOK_DISCORD")
DB = "db.json"
# Cabecera para la peticion a la API
CABECERA = { "User-Agent": "DealGameAlert Script" }
# Parametros de busqueda
PARAMETROS = { "upperPrice" : 0 }