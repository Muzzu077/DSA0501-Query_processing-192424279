"""
Experiment Number: 22
File Name: experiment_22.py
Description: Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    # X and Y axis values
    x = [1, 2, 3]
    y = [2, 4, 1]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue', marker='o')
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Sample graph!')
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_22_output.png'
    plt.savefig(output_path)
    print(f"Line plot created and saved as {output_path}")

if __name__ == '__main__':
    main()
