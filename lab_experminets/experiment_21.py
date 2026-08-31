"""
Experiment Number: 21
File Name: experiment_21.py
Description: Write a Pandas program to swap the cases of a specified character column in a given DataFrame.
"""

import pandas as pd

def main():
    data = {
        'company_code': ['c001', 'C002', 'c003', 'C004', 'c005'],
        'name': ['Google', 'MICROSOFT', 'apple', 'AMAZON', 'netflix']
    }
    
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    
    # Swapping the cases of specified character columns
    df['name_swapped'] = df['name'].str.swapcase()
    df['company_code_swapped'] = df['company_code'].str.swapcase()
    
    print("\nDataFrame after swapping cases of 'name' and 'company_code':")
    print(df)

if __name__ == '__main__':
    main()
