import sqlite3

con = sqlite3.connect("nis.db")
cur = con.cursor()

try:
    cur.execute("ALTER TABLE result ADD COLUMN marks_obtained INTEGER")
except:
    pass

try:
    cur.execute("ALTER TABLE result ADD COLUMN full_marks INTEGER")
except:
    pass

try:
    cur.execute("ALTER TABLE result ADD COLUMN per REAL")
except:
    pass

try:
    cur.execute("ALTER TABLE users ADD COLUMN name TEXT")
    print("✅ Column 'name' added successfully")
except Exception as e:
    print("⚠️ Error or column already exists:", e)


con.commit()
con.close()

print("All required columns checked/added successfully")
