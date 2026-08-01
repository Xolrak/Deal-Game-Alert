from api import obtener_tiendas, obtener_juegos_gratis, enviar_discord
from storage import importar_json, guardar_json

def main():
    # 1. Cargar datos iniciales
    enviados = importar_json()
    mapa_tiendas = obtener_tiendas()
    juegos = obtener_juegos_gratis()

    # 2. Recorrer y procesar
    for juego in juegos:
        oferta_id = juego["dealID"]

        if oferta_id in enviados:
            continue

        # Si no está enviado, obtener la tienda y mandar
        tienda_id = juego["storeID"]
        nombre_tienda = mapa_tiendas.get(tienda_id, "Tienda desconocida")

        enviar_discord(juego, nombre_tienda)

        # Guardar en el historial
        enviados.append(oferta_id)
        guardar_json(enviados)
        print(f"¡{juego['title']} enviado a Discord y registrado!")

if __name__ == "__main__":
    main()