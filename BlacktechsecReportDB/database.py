import sqlite3
from datetime import datetime

# Nombre del archivo de la base de datos
DB_NAME = "queries.db"


def init_db():
    # Crear conexión y tabla si no existe
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def save_query(question, answer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO queries (question, answer, created_at)
        VALUES (?, ?, ?)
    ''', (question, answer, datetime.now()))

    conn.commit()
    conn.close()