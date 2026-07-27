import json

def create_faculty_json():
    filename = "faculty.json"
    
    faculty_members = [
        {"Faculty ID": "FAC201", "Faculty Name": "Dr. Ramesh Chandra", "Department": "Computer Science", "Designation": "Professor & HOD", "Experience (Years)": 18},
        {"Faculty ID": "FAC202", "Faculty Name": "Dr. Shalini Iyer", "Department": "Data Science", "Designation": "Associate Professor", "Experience (Years)": 12},
        {"Faculty ID": "FAC203", "Faculty Name": "Prof. Nitin Saxena", "Department": "Artificial Intelligence", "Designation": "Assistant Professor", "Experience (Years)": 7},
        {"Faculty ID": "FAC204", "Faculty Name": "Dr. Aruna Hegde", "Department": "Information Technology", "Designation": "Professor", "Experience (Years)": 15},
        {"Faculty ID": "FAC205", "Faculty Name": "Prof. Sanjay Mishra", "Department": "Cyber Security", "Designation": "Assistant Professor", "Experience (Years)": 5}
    ]
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(faculty_members, file, indent=4)
        
    print(f"Successfully created '{filename}' with {len(faculty_members)} faculty members.")

def display_faculty_json():
    print("\n--- Reading 'faculty.json' ---")
    with open("faculty.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    create_faculty_json()
    display_faculty_json()
