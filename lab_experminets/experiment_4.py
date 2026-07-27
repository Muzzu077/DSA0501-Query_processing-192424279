"""
Experiment Number: 4
File Name: experiment_4.py
Description: Write a Pandas program to create a line plot of the historical stock prices of Alphabet Inc. between two specific dates.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    stock_data = {
        'Date': pd.to_datetime(['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06', '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-13', '2020-04-14', '2020-04-15', '2020-04-16', '2020-04-17', '2020-04-20', '2020-04-21', '2020-04-22', '2020-04-23', '2020-04-24', '2020-04-27', '2020-04-28', '2020-04-29', '2020-04-30', '2020-05-01']),
        'Open': [1122, 1098.26, 1119.015, 1138, 1221, 1206.5, 1224.08, 1209.18, 1245.09, 1245.61, 1274.1, 1284.85, 1271, 1247, 1245.54, 1271.55, 1261.17, 1296, 1287.93, 1341.46, 1324.88, 1328.5],
        'Close': [1105.62, 1120.84, 1097.88, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56, 1269.23, 1262.47, 1263.47, 1283.25, 1266.61, 1216.34, 1263.21, 1276.31, 1279.31, 1275.88, 1233.67, 1341.48, 1348.66, 1320.61]
    }
    
    df = pd.DataFrame(stock_data)
    start_date = '2020-04-01'
    end_date = '2020-04-20'
    
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    plt.figure(figsize=(10, 5))
    plt.plot(filtered_df['Date'], filtered_df['Close'], marker='o', color='b', label='Close Price')
    plt.title('Alphabet Inc. Historical Stock Prices (01-04-2020 to 20-04-2020)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/experiment_4_output.png')
    print("Alphabet stock line plot created and saved as outputs/experiment_4_output.png")

if __name__ == '__main__':
    main()
