import csv

def create_employees_csv():
    filename = "employees.csv"
    
    employees = [
        {"Employee ID": "EMP101", "Employee Name": "Rajesh Khanna", "Department": "Engineering", "Designation": "Senior Software Engineer", "Salary": 95000},
        {"Employee ID": "EMP102", "Employee Name": "Sunita Menon", "Department": "Human Resources", "Designation": "HR Manager", "Salary": 82000},
        {"Employee ID": "EMP103", "Employee Name": "Amitabh Roy", "Department": "Data Science", "Designation": "Lead Data Scientist", "Salary": 115000},
        {"Employee ID": "EMP104", "Employee Name": "Kavita Desai", "Department": "Finance", "Designation": "Financial Analyst", "Salary": 78000},
        {"Employee ID": "EMP105", "Employee Name": "Suresh Prabhu", "Department": "Operations", "Designation": "Operations Director", "Salary": 130000}
    ]
    
    headers = ["Employee ID", "Employee Name", "Department", "Designation", "Salary"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(employees)
        
    print(f"Successfully generated '{filename}' with {len(employees)} employee records.")

def display_employees():
    print("\n--- Reading 'employees.csv' ---")
    with open("employees.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<12} | {row[1]:<16} | {row[2]:<18} | {row[3]:<26} | ${float(row[4]):,.2f}" if row[0] != "Employee ID" else f"{row[0]:<12} | {row[1]:<16} | {row[2]:<18} | {row[3]:<26} | {row[4]}")

if __name__ == "__main__":
    create_employees_csv()
    display_employees()
