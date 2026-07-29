import sqlite3

def vehicle_registration_search_db():
    conn = sqlite3.connect("transport.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vehicle (
            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_number TEXT UNIQUE NOT NULL,
            owner_name TEXT NOT NULL,
            model TEXT NOT NULL,
            vehicle_type TEXT NOT NULL,
            reg_date TEXT NOT NULL
        )
    """)
    
    vehicles = [
        ("TN01AB1234", "Aarav Sharma", "Hyundai Creta", "SUV", "2024-03-15"),
        ("TN09CD5678", "Ananya Patel", "Honda City", "Sedan", "2023-11-20"),
        ("TN22EF9012", "Rohan Gupta", "Tata Nexon EV", "Electric SUV", "2025-01-10"),
        ("TN37GH3456", "Priya Nair", "Royal Enfield 350", "Two Wheeler", "2024-08-05")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Vehicle (reg_number, owner_name, model, vehicle_type, reg_date) VALUES (?, ?, ?, ?, ?)", vehicles)
    conn.commit()
    
    search_reg = "TN22EF9012"
    cursor.execute("SELECT * FROM Vehicle WHERE reg_number = ?", (search_reg,))
    search_result = cursor.fetchone()
    
    print(f"--- Vehicle Search Result for Reg No '{search_reg}' ---")
    if search_result:
        print(f"Vehicle ID     : {search_result[0]}")
        print(f"Reg Number     : {search_result[1]}")
        print(f"Owner Name     : {search_result[2]}")
        print(f"Model          : {search_result[3]}")
        print(f"Vehicle Type   : {search_result[4]}")
        print(f"Reg Date       : {search_result[5]}")
    else:
        print("Vehicle not found!")
        
    conn.close()

if __name__ == "__main__":
    vehicle_registration_search_db()
