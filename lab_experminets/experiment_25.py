"""
Experiment Number: 25
File Name: experiment_25.py
Description: Write a Python program to plot two or more lines with legends, different widths and colors.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    # Line 1 points
    x1 = [10, 20, 30]
    y1 = [20, 40, 10]
    
    # Line 2 points
    x2 = [10, 20, 30]
    y2 = [40, 10, 30]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x1, y1, color='blue', linewidth=3, label='line 1-width-3')
    plt.plot(x2, y2, color='red', linewidth=5, label='line 2-width-5')
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Two or more lines on same plot with suitable legends')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_25_output.png'
    plt.savefig(output_path)
    print(f"Multi-line plot created and saved as {output_path}")

if __name__ == '__main__':
    main()
