"""
Experiment Number: 11
File Name: experiment_11.py
Description: Create a dataframe of ten rows, four columns with random values. Convert some values to nan values. Write a Pandas program which will highlight the nan values.
"""

import pandas as pd
import numpy as np

def highlight_nan(val):
    color = 'background-color: red' if pd.isna(val) else ''
    return color

def main():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
    
    # Introduce NaN values
    df.iloc[0, 1] = np.nan
    df.iloc[2, 3] = np.nan
    df.iloc[5, 0] = np.nan
    df.iloc[8, 2] = np.nan

    print("Original DataFrame with NaN values:")
    print(df)

    styled_df = df.style.map(highlight_nan)
    print("\nDataFrame Styled with Highlighted NaN values (HTML Styler Object):")
    print(styled_df)

if __name__ == '__main__':
    main()
