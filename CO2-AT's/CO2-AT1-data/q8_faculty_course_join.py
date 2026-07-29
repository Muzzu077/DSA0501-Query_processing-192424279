import sqlite3

def university_faculty_course_db():
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Faculty (
            faculty_id INTEGER PRIMARY KEY,
            faculty_name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            course_code TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL,
            faculty_id INTEGER,
            FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
        )
    """)
    
    faculties = [
        (201, "Dr. Ramesh Chandra", "Computer Science"),
        (202, "Dr. Shalini Iyer", "Data Science"),
        (203, "Prof. Nitin Saxena", "AI & ML")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Faculty VALUES (?, ?, ?)", faculties)
    
    courses = [
        ("CS501", "Query Processing for Data Science", 4, 202),
        ("CS502", "Natural Language Processing", 3, 203),
        ("CS503", "Deep Learning & Vision", 4, 201),
        ("CS504", "Advanced Data Warehousing", 3, 202)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Course VALUES (?, ?, ?, ?)", courses)
    conn.commit()
    
    cursor.execute("""
        SELECT f.faculty_name, f.department, c.course_code, c.course_name, c.credits
        FROM Faculty f
        JOIN Course c ON f.faculty_id = c.faculty_id
    """)
    results = cursor.fetchall()
    
    print("--- Faculty Course Allocation (SQL JOIN Result) ---")
    print(f"{'Faculty Name':<20} | {'Department':<18} | {'Code':<8} | {'Course Title':<36} | {'Credits'}")
    print("-" * 92)
    for r in results:
        print(f"{r[0]:<20} | {r[1]:<18} | {r[2]:<8} | {r[3]:<36} | {r[4]}")
        
    conn.close()

if __name__ == "__main__":
    university_faculty_course_db()
