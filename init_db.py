import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
