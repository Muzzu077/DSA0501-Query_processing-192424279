"""
Experiment Number: 5
File Name: experiment_5.py
Description: Write a Pandas program to create a bar plot of the trading volume of Alphabet Inc. stock between two specific dates.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    stock_data = {
        'Date': pd.to_datetime(['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06', '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-13', '2020-04-14', '2020-04-15']),
        'Volume': [2343100, 1964900, 2313400, 2664700, 2387300, 1975100, 2175400, 1739800, 2470400, 1671700]
    }
    
    df = pd.DataFrame(stock_data)
    start_date = '2020-04-01'
    end_date = '2020-04-10'
    
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    plt.figure(figsize=(10, 5))
    plt.bar(filtered_df['Date'].dt.strftime('%Y-%m-%d'), filtered_df['Volume'], color='orange')
    plt.title('Trading Volume of Alphabet Inc. Stock')
    plt.xlabel('Date')
    plt.ylabel('Trading Volume')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/experiment_5_output.png')
    print("Trading volume bar plot created and saved as outputs/experiment_5_output.png")

if __name__ == '__main__':
    main()
