"""
Experiment Number: 34
File Name: experiment_34.py
Description: Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(42)
    n = 50
    x = np.random.rand(n)
    y = np.random.rand(n)
    colors = np.random.rand(n)
    area = (30 * np.random.rand(n)) ** 2  # 0 to 30 point radii
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='viridis')
    
    plt.xlabel('X (Random Values)')
    plt.ylabel('Y (Random Values)')
    plt.title('Scatter Plot with Balls of Different Sizes and Colors')
    plt.colorbar(label='Color Scale')
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_34_output.png'
    plt.savefig(output_path)
    print(f"Scatter plot with balls of different sizes created and saved as {output_path}")

if __name__ == '__main__':
    main()
