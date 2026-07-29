import sqlite3

def online_course_registration_db():
    conn = sqlite3.connect("online_course.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course_Registration (
            reg_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_name TEXT NOT NULL,
            registration_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(student_id)
        )
    """)
    
    students = [(101, "Aarav Sharma", "aarav@gmail.com"), (102, "Ananya Patel", "ananya@gmail.com"), (103, "Rohan Gupta", "rohan@gmail.com")]
    cursor.executemany("INSERT OR IGNORE INTO Student VALUES (?, ?, ?)", students)
    
    registrations = [
        (101, "Query Processing for Data Science", "2026-01-10"),
        (101, "Natural Language Processing", "2026-01-12"),
        (102, "Deep Learning Specialization", "2026-01-11"),
        (103, "Query Processing for Data Science", "2026-01-15")
    ]
    cursor.executemany("INSERT INTO Course_Registration (student_id, course_name, registration_date) VALUES (?, ?, ?)", registrations)
    conn.commit()
    
    cursor.execute("""
        SELECT s.student_id, s.student_name, cr.course_name, cr.registration_date
        FROM Student s
        JOIN Course_Registration cr ON s.student_id = cr.student_id
    """)
    results = cursor.fetchall()
    
    print("--- Student Course Registrations (SQL JOIN Result) ---")
    print(f"{'STD ID':<8} | {'Student Name':<16} | {'Registered Course':<38} | {'Date'}")
    print("-" * 80)
    for r in results:
        print(f"{r[0]:<8} | {r[1]:<16} | {r[2]:<38} | {r[3]}")
        
    conn.close()

if __name__ == "__main__":
    online_course_registration_db()
