import requests
import time
from src.config import WEBHOOK_DISCORD

def enviar_discord(juego: dict, nombre_tienda: str):

    if not WEBHOOK_DISCORD:
        print("Error: La constante WEBHOOK_DISCORD no esta configurada")
        return

    titulo = juego.get("title", "Juego sin titulo")
    precio_normal = juego.get("normalPrice", "0.00")
    descuento = round(float(juego.get("savings", 0)))
    imagen = juego.get("thumb", "")
    ofertaID = juego.get("dealID", "")
    url_oferta = f"https://www.cheapshark.com/redirect?dealID={ofertaID}"

    mensaje_discord = {
            "embeds": [
                {
                    "title": titulo,
                    "description": (
                        f"**Tienda:** {nombre_tienda}\n"
                        f"**Precio original:** ~~${precio_normal}~~ ¡GRATIS!\n"
                        f"**Descuento:** {descuento}%\n\n"
                        f"[👉 Reclamar juego en {nombre_tienda}]({url_oferta})"
                    ),
                    "color": 5763719,
                    "thumbnail": {
                        "url": imagen
                    }
                }
            ]
        }
    
    try:
        respuesta = requests.post(WEBHOOK_DISCORD, json=mensaje_discord, timeout=5)

        if respuesta.status_code == 429:
            tiempo_espera = respuesta.json().get("retry_after", 3)
            print(f"Rate limit alcanzado. Esperando {tiempo_espera}s para reintentar...")
            time.sleep(tiempo_espera)
            respuesta = requests.post(WEBHOOK_DISCORD, json=mensaje_discord, timeout=5)
        respuesta.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"Timeout al enviar '{titulo}' a Discord.")        
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP al notificar a Discord: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Error de red al enviar a Discord: {error}")
