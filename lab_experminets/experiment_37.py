"""
Experiment Number: 37
File Name: experiment_37.py
Description: Write a Pandas program to create a dataframe from a dictionary and display it.
"""

import pandas as pd

def main():
    sample_data = {
        'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]
    }
    
    df = pd.DataFrame(sample_data)
    print("DataFrame created from dictionary:")
    print(df)

if __name__ == '__main__':
    main()
