"""
Experiment Number: 14
File Name: experiment_14.py
Description: Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
"""

import pandas as pd
import numpy as np

def main():
    data = {
        'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, "--", 70010, 70003, 70012, np.nan, 70013],
        'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, "?", 2480.4, 250.45, 75.29, 3045.6],
        'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
        'customer_id': [3002, 3001, 3001, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
        'salesman_id': [5002, 5005, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5007, 5001]
    }
    
    df = pd.DataFrame(data)
    print("Original DataFrame with uninformative missing/placeholder values:")
    print(df)
    
    # Replace non-valuable information / placeholder strings with NaN
    df_cleaned = df.replace(['--', '?'], np.nan)
    print("\nDataFrame after replacing placeholder strings with NaN:")
    print(df_cleaned)

    # Fill NaN values with 0
    df_filled = df_cleaned.fillna(0)
    print("\nDataFrame after replacing missing values with 0:")
    print(df_filled)

if __name__ == '__main__':
    main()
