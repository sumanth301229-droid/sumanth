import sqlite3
import os

os.makedirs("healthcare_project/db", exist_ok=True)

conn = sqlite3.connect("healthcare_project/db/health.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS health_metrics (
    patient TEXT PRIMARY KEY,
    bp INTEGER,
    sugar INTEGER
)
""")

try:
    cursor.execute("INSERT INTO health_metrics VALUES (?, ?, ?)", ("Sai", 120, 90))
    cursor.execute("INSERT INTO health_metrics VALUES (?, ?, ?)", ("Sumanth", 120, 90))
    cursor.execute("INSERT INTO health_metrics VALUES (?, ?, ?)", ("Varsha",20, 90))
    cursor.execute("INSERT INTO health_metrics VALUES (?, ?, ?)", ("Amin", 120, 90))
    cursor.execute("INSERT INTO health_metrics VALUES (?, ?, ?)", ("Sandhya", 120, 90))
except:
    print("Duplicate entry skipped")

conn.commit()
conn.close()

print("Database created successfully")