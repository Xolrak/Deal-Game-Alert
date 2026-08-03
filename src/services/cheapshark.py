import requests
from src.config import URL_TIENDAS, CABECERA, URL_DESCUENTOS, PARAMETROS

def obtener_tiendas():
    try:
        respuesta_tiendas = requests.get(URL_TIENDAS, headers=CABECERA, timeout=5)
        respuesta_tiendas.raise_for_status()
        lista_tiendas = respuesta_tiendas.json()
        return {tienda["storeID"]: tienda["storeName"] for tienda in lista_tiendas}
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP: {error}")
    except requests.exceptions.Timeout as error:
        print(f"El servidor tardó demasiado en responder ({error})")
    except requests.exceptions.RequestException as error:
        print(f"Ocurrió un error en la petición: {error}")

    return {} # devuelve diccionario vacio si hay error

def obtener_juegos_gratis():
    try:
        respuesta_juegos = requests.get(URL_DESCUENTOS, params=PARAMETROS, headers=CABECERA, timeout=5)
        respuesta_juegos.raise_for_status()
        return respuesta_juegos.json()
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP: {error}")
    except requests.exceptions.Timeout:
        print(f"El servidor tardó demasiado en responder")
    except requests.exceptions.RequestException as error:
        print(f"Ocurrió un error en la petición: {error}")

    return [] # devuelve diccionario vacio si hay error