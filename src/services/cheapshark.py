import requests
from src.config import URL_TIENDAS, CABECERA, URL_DESCUENTOS, PARAMETROS

def obtener_tiendas():
    respuesta_tiendas = requests.get(URL_TIENDAS, headers=CABECERA)
    lista_tiendas = respuesta_tiendas.json()
    return {tienda["storeID"]: tienda["storeName"] for tienda in lista_tiendas}

def obtener_juegos_gratis():
    respuesta_juegos = requests.get(URL_DESCUENTOS, params=PARAMETROS, headers=CABECERA) 
    return respuesta_juegos.json()