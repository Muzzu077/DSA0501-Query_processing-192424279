"""
Experiment Number: 18
File Name: experiment_18.py
Description: Write a Pandas program to split the following given dataframe into groups based on school code and class.
"""

import pandas as pd

def main():
    student_data = {
        'school_code': ['s001', 's002', 's001', 's002', 's001', 's003'],
        'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
        'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
        'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
        'age': [12, 12, 13, 13, 14, 12],
        'height': [173, 192, 186, 167, 151, 159],
        'weight': [35, 32, 33, 30, 31, 32],
        'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
    }
    
    df = pd.DataFrame(student_data)
    print("Original DataFrame:")
    print(df)
    
    grouped = df.groupby(['school_code', 'class'])
    print("\nGroup data by school code and class:")
    for (school, cls), group in grouped:
        print(f"\nGroup - School Code: {school}, Class: {cls}")
        print(group)

if __name__ == '__main__':
    main()
