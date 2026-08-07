"""
Experiment Number: 20
File Name: experiment_20.py
Description: Write a Pandas program to find the index of a given substring of a DataFrame column.
"""

import pandas as pd

def main():
    data = {
        'name_code': ['Company_Apple', 'Company_Google', 'Company_Microsoft', 'Inc_Amazon', 'Corp_Meta', 'Company_Netflix']
    }
    
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    
    substring = 'Company'
    
    # Character start index of substring in each row string (-1 if not found)
    df['substring_char_index'] = df['name_code'].str.find(substring)
    
    # Row indices where substring exists
    matching_row_indices = df[df['name_code'].str.contains(substring)].index.tolist()
    
    print(f"\nCharacter start index of substring '{substring}' in column 'name_code':")
    print(df[['name_code', 'substring_char_index']])
    
    print(f"\nRow indices containing substring '{substring}':")
    print(matching_row_indices)

if __name__ == '__main__':
    main()
