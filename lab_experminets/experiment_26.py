"""
Experiment Number: 26
File Name: experiment_26.py
Description: Write a Python program to create multiple plots.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 2 * np.pi, 400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    ax1.plot(x, y1, color='blue', label='sin(x)')
    ax1.set_title('Sine Wave')
    ax1.set_xlabel('x')
    ax1.set_ylabel('sin(x)')
    ax1.grid(True)
    ax1.legend()
    
    ax2.plot(x, y2, color='orange', label='cos(x)')
    ax2.set_title('Cosine Wave')
    ax2.set_xlabel('x')
    ax2.set_ylabel('cos(x)')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    output_path = 'outputs/experiment_26_output.png'
    plt.savefig(output_path)
    print(f"Multiple plots created and saved as {output_path}")

if __name__ == '__main__':
    main()
