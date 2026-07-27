import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def create_courses_xml():
    filename = "courses.xml"
    
    courses = [
        {"Course Code": "CS501", "Course Name": "Advanced Query Processing & Optimization", "Credits": 4, "Department": "Data Science", "Faculty Name": "Dr. Shalini Iyer"},
        {"Course Code": "CS502", "Course Name": "Natural Language Processing", "Credits": 3, "Department": "Artificial Intelligence", "Faculty Name": "Prof. Nitin Saxena"},
        {"Course Code": "CS503", "Course Name": "Deep Learning & Computer Vision", "Credits": 4, "Department": "Computer Science", "Faculty Name": "Dr. Ramesh Chandra"},
        {"Course Code": "CS504", "Course Name": "Cloud Computing Infrastructure", "Credits": 3, "Department": "Information Technology", "Faculty Name": "Dr. Aruna Hegde"},
        {"Course Code": "CS505", "Course Name": "Applied Cybersecurity & Forensics", "Credits": 4, "Department": "Cyber Security", "Faculty Name": "Prof. Sanjay Mishra"}
    ]
    
    root = ET.Element("courses")
    
    for c in courses:
        course_elem = ET.SubElement(root, "course")
        for key, val in c.items():
            tag = key.replace(" ", "_")
            child = ET.SubElement(course_elem, tag)
            child.text = str(val)
            
    raw_xml = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(raw_xml)
    pretty_xml = "
".join([line for line in parsed.toprettyxml(indent="  ").splitlines() if line.strip()])
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(pretty_xml)
        
    print(f"Successfully generated '{filename}' with {len(courses)} courses.")

def display_courses_xml():
    print("\n--- Reading 'courses.xml' ---")
    with open("courses.xml", "r", encoding="utf-8") as file:
        print(file.read())

if __name__ == "__main__":
    create_courses_xml()
    display_courses_xml()
