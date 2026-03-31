import sqlite3

conn = sqlite3.connect("healthcare_project/db/health.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM health_metrics")
rows = cursor.fetchall()

# Display data
for row in rows:
    print(row)

conn.close()