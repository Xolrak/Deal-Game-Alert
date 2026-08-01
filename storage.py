import sqlite3
from pathlib import Path
from config import DB_FILE

def inicializar_db():
    """
    Crea la tabla de ofertas en caso de no existir
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ofertas_notificadas (
                oferta_id TEXT PRIMARY KEY,
                titulo TEXT,
                tienda TEXT,
                precio_original FLOAT,
                precio_oferta FLOAT,
                fecha_notificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def comprobar_notificacion_enviada(oferta_id: str) -> bool:
    """
    Comprueba si la oferta fue notificada
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM ofertas_notificadas WHERE oferta_id = ?", (oferta_id,))
        return cursor.fetchone() is not None

def guardar_notificacion_enviada(oferta_id: str, titulo:str, tienda:str, precio_original:float, precio_oferta:float):
    """
    Guarda un nuevo ID de oferta en la base de datos
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO ofertas_notificadas (oferta_id, titulo, tienda, precio_original, precio_oferta)
            VALUES (?, ?, ?, ?, ?)
        """, (oferta_id, titulo, tienda, precio_original, precio_oferta))
        conn.commit()