"""
Experiment Number: 38
File Name: experiment_38.py
Description: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
"""

import pandas as pd
import numpy as np

def main():
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    df = pd.DataFrame(exam_data, index=labels)
    print("DataFrame with specified index labels:")
    print(df)

if __name__ == '__main__':
    main()
