import sqlite3
import datetime

data = sqlite3.connect("test_database")
cursor = sqlite3.Cursor(data)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Aarav", 20)
)

cursor.execute(
    "DELETE FROM students"
)

data.commit()
data.close()