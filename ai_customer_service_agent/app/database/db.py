import sqlite3

def get_conn():
    return sqlite3.connect("data/tickets.db")

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        category TEXT,
        department TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()
