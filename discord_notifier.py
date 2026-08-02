# discord_notifier.py
import requests
from config import WEBHOOK_DISCORD

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
    
    if not WEBHOOK_DISCORD:
        print("Error: La constante WEBHOOK_DISCORD no está configurada")
    else:
        requests.post(WEBHOOK_DISCORD, json=mensaje_discord)