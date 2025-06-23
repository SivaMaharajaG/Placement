# placement_chatbot_app/db/database.py
import sqlite3

def init_db():
    conn = sqlite3.connect("data/chat_history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            qualification TEXT,
            role TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            username TEXT,
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()
    conn.close()
