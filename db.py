# db.py - simple SQLite storage for BMI records
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'bmi_records.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        bmi REAL NOT NULL,
        category TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def add_record(weight, height, bmi, category, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO records (weight, height, bmi, category, timestamp) VALUES (?,?,?,?,?)',
              (weight, height, bmi, category, timestamp))
    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, weight, height, bmi, category, timestamp FROM records ORDER BY timestamp')
    rows = c.fetchall()
    conn.close()
    return rows
