from api import obtener_tiendas, obtener_juegos_gratis, enviar_discord
from storage import inicializar_db, comprobar_notificacion_enviada, guardar_notificacion_enviada

def main():
    # 1. Cargar datos iniciales
    inicializar_db()
    mapa_tiendas = obtener_tiendas()
    juegos = obtener_juegos_gratis()

    # 2. Recorrer y procesar
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

if __name__ == "__main__":
    main()