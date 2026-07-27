"""
Experiment Number: 6
File Name: experiment_6.py
Description: Write a Pandas program to create a scatter plot of the trading volume/stock prices of Alphabet Inc. stock between two specific dates.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    stock_data = {
        'Date': pd.to_datetime(['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06', '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-13', '2020-04-14', '2020-04-15']),
        'Close': [1105.62, 1120.84, 1097.88, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56, 1269.23, 1262.47],
        'Volume': [2343100, 1964900, 2313400, 2664700, 2387300, 1975100, 2175400, 1739800, 2470400, 1671700]
    }
    
    df = pd.DataFrame(stock_data)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Volume'], df['Close'], color='red')
    plt.title('Trading Volume vs Stock Price of Alphabet Inc.')
    plt.xlabel('Trading Volume')
    plt.ylabel('Stock Close Price')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('outputs/experiment_6_output.png')
    print("Scatter plot created and saved as outputs/experiment_6_output.png")

if __name__ == '__main__':
    main()
