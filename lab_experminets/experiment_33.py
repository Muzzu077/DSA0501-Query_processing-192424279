"""
Experiment Number: 33
File Name: experiment_33.py
Description: Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(42)
    x = np.random.randn(100)
    y = np.random.randn(100)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, facecolors='none', edgecolors='green', s=80, linewidths=1.5)
    
    plt.xlabel('X (Random Distribution)')
    plt.ylabel('Y (Random Distribution)')
    plt.title('Scatter Plot with Empty Circles')
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_33_output.png'
    plt.savefig(output_path)
    print(f"Scatter plot with empty circles created and saved as {output_path}")

if __name__ == '__main__':
    main()
