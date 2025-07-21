import sqlite3
import csv
from datetime import datetime

DB_NAME = "queries.db"
CSV_FILENAME = f"consultas_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

def export_to_csv():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, question, answer, created_at FROM queries ORDER BY id ASC")
    rows = cursor.fetchall()

    with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Pregunta", "Respuesta", "Fecha de creación"])
        writer.writerows(rows)

    conn.close()
    print(f"\n✅ Exportación completa. Archivo creado: {CSV_FILENAME}")

if __name__ == "__main__":
    export_to_csv()
