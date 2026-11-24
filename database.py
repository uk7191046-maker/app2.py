
import sqlite3

conn = sqlite3.connect("students.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()
conn.close()
print("database")
