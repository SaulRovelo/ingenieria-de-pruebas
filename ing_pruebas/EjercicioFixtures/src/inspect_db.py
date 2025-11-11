import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("📋 Tablas disponibles:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = [t[0] for t in cursor.fetchall()]
    for t in tablas:
        print(f" - {t}")

    print("\n📌 Esquema de cada tabla:")
    for tabla in tablas:
        print(f"\n🔹 Tabla: {tabla}")
        cursor.execute(f"PRAGMA table_info({tabla});")
        columnas = cursor.fetchall()
        df_columnas = pd.DataFrame(
            columnas,
            columns=["cid", "name", "type", "notnull", "dflt_value", "pk"]
        )
        print(df_columnas)

    print("\n📊 Ejemplo de contenido:")
    for tabla in tablas:
        print(f"\n🔹 Contenido de {tabla}:")
        df = pd.read_sql_query(f"SELECT * FROM {tabla} LIMIT 5;", conn)
        print(df)

    conn.close()

if __name__ == "__main__":
    main()
