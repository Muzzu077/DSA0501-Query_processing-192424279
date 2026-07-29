import sqlite3

def company_employee_department_db():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            dept_id INTEGER PRIMARY KEY,
            dept_name TEXT NOT NULL UNIQUE,
            location TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL CHECK(salary > 0),
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        )
    """)
    
    departments = [(10, "Engineering", "Building A"), (20, "Data Analytics", "Building B"), (30, "Human Resources", "Building C")]
    cursor.executemany("INSERT OR IGNORE INTO Department VALUES (?, ?, ?)", departments)
    
    employees = [
        ("Rajesh Khanna", "Senior Engineer", 95000, 10),
        ("Sunita Menon", "Data Scientist", 105000, 20),
        ("Amitabh Roy", "HR Executive", 65000, 30),
        ("Kavita Desai", "DevOps Engineer", 88000, 10),
        ("Suresh Prabhu", "BI Analyst", 82000, 20)
    ]
    cursor.executemany("INSERT INTO Employee (emp_name, designation, salary, dept_id) VALUES (?, ?, ?, ?)", employees)
    conn.commit()
    
    cursor.execute("""
        SELECT e.emp_id, e.emp_name, e.designation, d.dept_name, d.location
        FROM Employee e
        JOIN Department d ON e.dept_id = d.dept_id
    """)
    results = cursor.fetchall()
    
    print("--- Employee Details with Department (SQL JOIN Result) ---")
    print(f"{'EMP ID':<8} | {'Employee Name':<16} | {'Designation':<18} | {'Department':<18} | {'Location'}")
    print("-" * 80)
    for r in results:
        print(f"{r[0]:<8} | {r[1]:<16} | {r[2]:<18} | {r[3]:<18} | {r[4]}")
        
    conn.close()

if __name__ == "__main__":
    company_employee_department_db()
