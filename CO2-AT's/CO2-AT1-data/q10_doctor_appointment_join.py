import sqlite3

def hospital_appointment_db():
    conn = sqlite3.connect("hospital_appointments.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INTEGER PRIMARY KEY,
            doctor_name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor_id INTEGER,
            appointment_date TEXT NOT NULL,
            time_slot TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
        )
    """)
    
    doctors = [
        (501, "Dr. A. K. Kapoor", "Cardiology", "9811122233"),
        (502, "Dr. Meenakshi Rao", "Endocrinology", "9811144455"),
        (503, "Dr. R. C. Joshi", "Orthopedics", "9811166677")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Doctor VALUES (?, ?, ?, ?)", doctors)
    
    appointments = [
        ("Suresh Sen", 501, "2026-08-01", "10:00 AM", "Confirmed"),
        ("Sunita Patil", 502, "2026-08-01", "11:30 AM", "Confirmed"),
        ("Anita Sharma", 503, "2026-08-02", "02:00 PM", "Scheduled"),
        ("Deepak Tiwari", 501, "2026-08-02", "03:30 PM", "Confirmed")
    ]
    cursor.executemany("INSERT INTO Appointment (patient_name, doctor_id, appointment_date, time_slot, status) VALUES (?, ?, ?, ?, ?)", appointments)
    conn.commit()
    
    cursor.execute("""
        SELECT a.appointment_id, a.patient_name, d.doctor_name, d.specialization, a.appointment_date, a.time_slot, a.status
        FROM Appointment a
        JOIN Doctor d ON a.doctor_id = d.doctor_id
    """)
    results = cursor.fetchall()
    
    print("--- Hospital Doctor Appointment Details (SQL JOIN Result) ---")
    print(f"{'APPT ID':<8} | {'Patient Name':<16} | {'Doctor Name':<18} | {'Specialization':<16} | {'Date':<10} | {'Time':<10} | {'Status'}")
    print("-" * 102)
    for r in results:
        print(f"{r[0]:<8} | {r[1]:<16} | {r[2]:<18} | {r[3]:<16} | {r[4]:<10} | {r[5]:<10} | {r[6]}")
        
    conn.close()

if __name__ == "__main__":
    hospital_appointment_db()
