import sqlite3
import os

# Database file name
db_name = "nis.db"
def create_database():


# Connect to database
    con = sqlite3.connect("nis.db")
    cur = con.cursor()

    # === COURSE TABLE ===
    cur.execute("""
    CREATE TABLE IF NOT EXISTS course(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        duration TEXT,
        charges TEXT,
        description TEXT
    )
    """)

    # === STUDENT TABLE ===
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        admission TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)

    #==================result table ==================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result(      
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll INTEGER,
        name TEXT,
        course TEXT,
        marks_obtained TEXT,
        full_marks TEXT, per text
                
    )
    """)

    con.commit()
    con.close()

print("Database and tables created successfully.")

create_database()