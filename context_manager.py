import sqlite3
from contextlib import contextmanager

@contextmanager
def connect(path):
    conn = sqlite3.connect(path)
    try:
        yield conn
    finally:
        conn.close()


with connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM example")
    for row in cursor.fetchall():
        print(row)