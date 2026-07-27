import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def create_patients_xml():
    filename = "patients.xml"
    
    patients = [
        {"Patient ID": "PAT301", "Patient Name": "Suresh Sen", "Age": 45, "Disease": "Hypertension", "Doctor Assigned": "Dr. A. K. Kapoor"},
        {"Patient ID": "PAT302", "Patient Name": "Sunita Patil", "Age": 32, "Disease": "Type 2 Diabetes", "Doctor Assigned": "Dr. Meenakshi Rao"},
        {"Patient ID": "PAT303", "Patient Name": "Ramesh Bose", "Age": 61, "Disease": "Coronary Artery Disease", "Doctor Assigned": "Dr. V. S. Agarwal"},
        {"Patient ID": "PAT304", "Patient Name": "Anita Sharma", "Age": 28, "Disease": "Acute Bronchitis", "Doctor Assigned": "Dr. S. N. Banerjee"},
        {"Patient ID": "PAT305", "Patient Name": "Mahesh Bhat", "Age": 54, "Disease": "Osteoarthritis", "Doctor Assigned": "Dr. R. C. Joshi"},
        {"Patient ID": "PAT306", "Patient Name": "Pooja Malhotra", "Age": 39, "Disease": "Migraine", "Doctor Assigned": "Dr. Meenakshi Rao"},
        {"Patient ID": "PAT307", "Patient Name": "Vijay Pillai", "Age": 70, "Disease": "Pneumonia", "Doctor Assigned": "Dr. S. N. Banerjee"},
        {"Patient ID": "PAT308", "Patient Name": "Kavita Sethi", "Age": 24, "Disease": "Appendicitis", "Doctor Assigned": "Dr. A. K. Kapoor"},
        {"Patient ID": "PAT309", "Patient Name": "Deepak Tiwari", "Age": 48, "Disease": "Gastritis", "Doctor Assigned": "Dr. R. C. Joshi"},
        {"Patient ID": "PAT310", "Patient Name": "Rekha Nambiar", "Age": 56, "Disease": "Hypothyroidism", "Doctor Assigned": "Dr. Meenakshi Rao"}
    ]
    
    root = ET.Element("patients")
    
    for p in patients:
        patient_elem = ET.SubElement(root, "patient")
        for key, val in p.items():
            tag = key.replace(" ", "_")
            child = ET.SubElement(patient_elem, tag)
            child.text = str(val)
            
    raw_xml = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(raw_xml)
    pretty_xml = "
".join([line for line in parsed.toprettyxml(indent="  ").splitlines() if line.strip()])
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(pretty_xml)
        
    print(f"Successfully generated '{filename}' containing {len(patients)} patient records.")

def display_patients_xml():
    print("\n--- Reading 'patients.xml' ---")
    with open("patients.xml", "r", encoding="utf-8") as file:
        print(file.read())

if __name__ == "__main__":
    create_patients_xml()
    display_patients_xml()
