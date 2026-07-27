import csv

def create_student_marks_csv():
    filename = "student_marks.csv"
    
    students = [
        {"Register Number": "192424001", "Student Name": "Aarav Sharma", "Department": "Computer Science", "Python Marks": 92, "Data Science Marks": 88},
        {"Register Number": "192424002", "Student Name": "Ananya Patel", "Department": "Data Science", "Python Marks": 95, "Data Science Marks": 91},
        {"Register Number": "192424003", "Student Name": "Rohan Gupta", "Department": "Artificial Intelligence", "Python Marks": 85, "Data Science Marks": 89},
        {"Register Number": "192424004", "Student Name": "Priya Nair", "Department": "Computer Science", "Python Marks": 78, "Data Science Marks": 84},
        {"Register Number": "192424005", "Student Name": "Vikram Singh", "Department": "Information Technology", "Python Marks": 88, "Data Science Marks": 86},
        {"Register Number": "192424006", "Student Name": "Sneha Reddy", "Department": "Data Science", "Python Marks": 94, "Data Science Marks": 96},
        {"Register Number": "192424007", "Student Name": "Karan Kumar", "Department": "Cyber Security", "Python Marks": 81, "Data Science Marks": 79},
        {"Register Number": "192424008", "Student Name": "Divya Verma", "Department": "Artificial Intelligence", "Python Marks": 90, "Data Science Marks": 92},
        {"Register Number": "192424009", "Student Name": "Rahul Das", "Department": "Computer Science", "Python Marks": 87, "Data Science Marks": 83},
        {"Register Number": "192424010", "Student Name": "Meera Joshi", "Department": "Data Science", "Python Marks": 96, "Data Science Marks": 94}
    ]
    
    headers = ["Register Number", "Student Name", "Department", "Python Marks", "Data Science Marks"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)
        
    print(f"Successfully generated '{filename}' with {len(students)} student records.")

def display_student_marks():
    print("\n--- Reading 'student_marks.csv' ---")
    with open("student_marks.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<17} | {row[1]:<16} | {row[2]:<24} | {row[3]:<12} | {row[4]:<18}")

if __name__ == "__main__":
    create_student_marks_csv()
    display_student_marks()
