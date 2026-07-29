import sqlite3

def hospital_patient_crud_db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER CHECK(age > 0),
            disease TEXT NOT NULL,
            contact TEXT NOT NULL,
            status TEXT DEFAULT 'Admitted'
        )
    """)
    
    patients = [
        ("Suresh Sen", 45, "Hypertension", "9876543210", "Admitted"),
        ("Sunita Patil", 32, "Type 2 Diabetes", "9876543211", "Admitted"),
        ("Ramesh Bose", 61, "Cardiac Care", "9876543212", "Discharged"),
        ("Anita Sharma", 28, "Acute Bronchitis", "9876543213", "Admitted"),
        ("Mahesh Bhat", 54, "Osteoarthritis", "9876543214", "Discharged")
    ]
    cursor.executemany("INSERT INTO Patient (name, age, disease, contact, status) VALUES (?, ?, ?, ?, ?)", patients)
    conn.commit()
    
    cursor.execute("UPDATE Patient SET contact = ? WHERE name = ?", ("9998887770", "Suresh Sen"))
    cursor.execute("DELETE FROM Patient WHERE status = 'Discharged'")
    conn.commit()
    
    cursor.execute("SELECT * FROM Patient")
    records = cursor.fetchall()
    
    print("--- Remaining Active Patients in Hospital ---")
    print(f"{'ID':<4} | {'Patient Name':<16} | {'Age':<5} | {'Disease':<18} | {'Updated Contact':<15} | {'Status'}")
    print("-" * 80)
    for p in records:
        print(f"{p[0]:<4} | {p[1]:<16} | {p[2]:<5} | {p[3]:<18} | {p[4]:<15} | {p[5]}")
        
    conn.close()

if __name__ == "__main__":
    hospital_patient_crud_db()
