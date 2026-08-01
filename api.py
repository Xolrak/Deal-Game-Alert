import requests
from config import URL_TIENDAS, CABECERA, URL_DESCUENTOS, PARAMETROS, WEBHOOK_DISCORD

def obtener_tiendas():
    respuesta_tiendas = requests.get(URL_TIENDAS, headers=CABECERA)
    lista_tiendas = respuesta_tiendas.json()
    return {tienda["storeID"]: tienda["storeName"] for tienda in lista_tiendas}

def obtener_juegos_gratis():
    respuesta_juegos = requests.get(URL_DESCUENTOS, params=PARAMETROS, headers=CABECERA) 
    return respuesta_juegos.json()

def enviar_discord(juego, nombre_tienda):
    titulo = juego["title"]
    precio_normal = juego["normalPrice"]
    descuento = round(float(juego["savings"]))
    imagen = juego["thumb"]
    ofertaID = juego["dealID"]
    url_oferta = f"https://www.cheapshark.com/redirect?dealID={ofertaID}"

    mensaje_discord = {
        "embeds": [
            {
                "title": f"{titulo}",
                "description": f"**Tienda:** {nombre_tienda}\n**Precio original:** ~~${precio_normal}~~ ¡GRATIS!\n**Descuento:** {descuento}%\n\n [Reclamar juego en {nombre_tienda}]({url_oferta})",
                "color": 5763719,
                "thumbnail": {
                    "url": imagen
                }
            }
        ]
    }

    requests.post(WEBHOOK_DISCORD, json=mensaje_discord)