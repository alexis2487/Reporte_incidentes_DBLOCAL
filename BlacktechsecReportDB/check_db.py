import sqlite3

DB_NAME = "queries.db"

def show_all_queries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, question, answer, created_at FROM queries ORDER BY id DESC")
    rows = cursor.fetchall()

    print(f"\n🧠 Historial de consultas (total: {len(rows)}):\n")
    for row in rows:
        print(f"🆔 ID: {row[0]}")
        print(f"❓ Pregunta: {row[1]}")
        print(f"✅ Respuesta: {row[2][:100]}...")  # recorta respuesta para vista rápida
        print(f"🕒 Fecha: {row[3]}")
        print("-" * 40)

    conn.close()

if __name__ == "__main__":
    show_all_queries()
