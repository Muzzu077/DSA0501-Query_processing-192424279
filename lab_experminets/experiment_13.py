"""
Experiment Number: 13
File Name: experiment_13.py
Description: Write a Pandas program to detect missing values of a given DataFrame. Display True or False.
"""

import pandas as pd
import numpy as np

def main():
    data = {
        'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
        'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
        'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
        'customer_id': [3002, 3001, 3001, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
        'salesman_id': [5002, 5005, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5007, 5001]
    }
    
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    
    print("\nDetect Missing Values (True for Missing, False for Present):")
    print(df.isna())

if __name__ == '__main__':
    main()
