"""
Experiment Number: 32
File Name: experiment_32.py
Description: Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.
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
    plt.scatter(x, y, color='blue', alpha=0.7)
    
    plt.xlabel('X (Random Normal Distribution)')
    plt.ylabel('Y (Random Normal Distribution)')
    plt.title('Scatter Graph of Random Distribution in X and Y')
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_32_output.png'
    plt.savefig(output_path)
    print(f"Scatter graph created and saved as {output_path}")

if __name__ == '__main__':
    main()
