"""
Experiment Number: 10
File Name: experiment_10.py
Description: Create a dataframe of ten rows, four columns with random values. Write a Pandas program to highlight the negative numbers red and positive numbers black.
"""

import pandas as pd
import numpy as np

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

def main():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
    print("Original DataFrame:")
    print(df)
    
    styled_df = df.style.map(color_negative_red)
    print("\nDataFrame Styled (HTML representation available when rendered):")
    print(styled_df)

if __name__ == '__main__':
    main()
