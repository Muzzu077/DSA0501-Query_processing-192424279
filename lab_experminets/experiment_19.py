"""
Experiment Number: 19
File Name: experiment_19.py
Description: Write a Pandas program to display the dimensions or shape of the World alcohol consumption dataset. Also extract the column names from the dataset.
"""

import pandas as pd

def main():
    world_alcohol_data = {
        'Year': [1986, 1986, 1985, 1986, 1987, 1987, 1987, 1985, 1986, 1984],
        'WHO region': ['Western Pacific', 'Europe', 'Africa', 'Americas', 'Americas', 'Americas', 'Europe', 'Africa', 'Americas', 'Africa'],
        'Country': ['Viet Nam', 'Uruguay', 'Cote d\'Ivoire', 'Colombia', 'Saint Kitts and Nevis', 'Guatemala', 'Azerbaijan', 'Angola', 'Antigua and Barbuda', 'Nigeria'],
        'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer', 'Other', 'Other', 'Spirits', 'Spirits', 'Other'],
        'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98, 0.00, 5.00, 0.39, 1.55, 6.10]
    }
    
    df = pd.DataFrame(world_alcohol_data)
    print("World Alcohol Consumption Dataset:")
    print(df)
    
    print("\nDataset Dimensions / Shape (Rows, Columns):")
    print(df.shape)
    
    print("\nColumn Names:")
    print(df.columns.tolist())

if __name__ == '__main__':
    main()
