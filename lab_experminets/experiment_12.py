"""
Experiment Number: 12
File Name: experiment_12.py
Description: Create a dataframe of ten rows, four columns with random values. Write a Pandas program to set dataframe background Color black and font color yellow.
"""

import pandas as pd
import numpy as np

def main():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
    
    print("Original DataFrame:")
    print(df)
    
    styled_df = df.style.set_properties(**{
        'background-color': 'black',
        'color': 'yellow'
    })
    
    print("\nDataFrame Styled with Black Background and Yellow Font (HTML Styler Object):")
    print(styled_df)

if __name__ == '__main__':
    main()
