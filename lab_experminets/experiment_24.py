"""
Experiment Number: 24
File Name: experiment_24.py
Description: Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('fdata.csv')
    print("Financial Data:")
    print(df)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Open'], label='Open', marker='o')
    plt.plot(df['Date'], df['High'], label='High', marker='s')
    plt.plot(df['Date'], df['Low'], label='Low', marker='^')
    plt.plot(df['Date'], df['Close'], label='Close', marker='d')
    
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Financial data of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_24_output.png'
    plt.savefig(output_path)
    print(f"Financial line charts created and saved as {output_path}")

if __name__ == '__main__':
    main()
