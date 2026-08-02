import sys
import subprocess
from src.storage import inicializar_db, comprobar_notificacion_enviada, guardar_notificacion_enviada
from src.services.cheapshark import obtener_tiendas, obtener_juegos_gratis
from src.notifiers.discord import enviar_discord

def limpiar_consola():
    """Limpia la pantalla de la terminal según el sistema operativo"""
    comando = 'cls' if sys.platform == 'win32' else 'clear'
    subprocess.run(comando, shell=True)

def mostrar_banner():
    """Muestra el nombre y estado del bot en la consola"""
    print("=" * 50)
    print("DEAL GAME ALERT BOT".center(50))
    print("=" * 50)

def main():
    # Limpiar terminal y mostrar banner
    limpiar_consola()
    mostrar_banner()

    # Cargar datos iniciales
    inicializar_db()
    mapa_tiendas = obtener_tiendas()
    juegos = obtener_juegos_gratis()

    nuevas_ofertas = 0
    # Recorrer y procesar
    for juego in juegos:
        oferta_id = juego["dealID"]

        if comprobar_notificacion_enviada(oferta_id):
            continue

        # Si no está enviado, obtener la tienda y mandar
        tienda_id = juego["storeID"]
        nombre_tienda = mapa_tiendas.get(tienda_id, "Tienda desconocida")
        enviar_discord(juego, nombre_tienda)

        precio_original = float(juego["normalPrice"])
        precio_oferta = float(juego["salePrice"])

        # Guardar en el historial
        guardar_notificacion_enviada(juego["dealID"], juego["title"], nombre_tienda, precio_original, precio_oferta)
        print(f"¡{juego['title']} enviado a Discord y registrado!")
        nuevas_ofertas += 1

    if nuevas_ofertas == 0:
        print("ℹNo hay nuevas ofertas para notificar.")

if __name__ == "__main__":
    main()