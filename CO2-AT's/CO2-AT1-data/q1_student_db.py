import sqlite3

def setup_student_database():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            gpa REAL CHECK(gpa >= 0.0 AND gpa <= 10.0)
        )
    """)
    
    students = [
        ("192424001", "Aarav Sharma", "Computer Science", 8.85),
        ("192424002", "Ananya Patel", "Data Science", 9.12),
        ("192424003", "Rohan Gupta", "Artificial Intelligence", 8.45),
        ("192424004", "Priya Nair", "Information Technology", 8.90),
        ("192424005", "Vikram Singh", "Cyber Security", 8.75)
    ]
    
    cursor.executemany("""
        INSERT OR IGNORE INTO Student (reg_no, name, department, gpa)
        VALUES (?, ?, ?, ?)
    """, students)
    
    conn.commit()
    
    cursor.execute("SELECT * FROM Student")
    records = cursor.fetchall()
    
    print("--- Student Database Records ---")
    print(f"{'ID':<5} | {'Register No':<12} | {'Student Name':<16} | {'Department':<24} | {'GPA':<5}")
    print("-" * 72)
    for row in records:
        print(f"{row[0]:<5} | {row[1]:<12} | {row[2]:<16} | {row[3]:<24} | {row[4]:<5.2f}")
        
    conn.close()

if __name__ == "__main__":
    setup_student_database()
