import os
import json
from config import DB

def importar_json():
    if (os.path.exists(DB)):
        with open(DB, "r") as archivo:
            return json.load(archivo)
    else:
        return []

def guardar_json(juegos):
    with open(DB, "w", encoding="utf-8") as archivo:
        json.dump(juegos, archivo, indent=4)