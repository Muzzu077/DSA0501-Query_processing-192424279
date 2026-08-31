"""
Experiment Number: 36
File Name: experiment_36.py
Description: Write a Python program to draw a scatter plot for three different groups comparing weights and heights.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(42)
    
    # Group 1 (Weight and Height)
    weight1 = np.array([67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56])
    height1 = np.array([101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 128.9, 132.8])
    
    # Group 2
    weight2 = np.array([61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6])
    height2 = np.array([152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1])
    
    # Group 3
    weight3 = np.array([68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7])
    height3 = np.array([165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3])
    
    plt.figure(figsize=(9, 6))
    plt.scatter(weight1, height1, marker='*', color='red', label='Group 1')
    plt.scatter(weight2, height2, marker='o', color='green', label='Group 2')
    plt.scatter(weight3, height3, marker='^', color='blue', label='Group 3')
    
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Group wise Weight vs Height comparison')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_36_output.png'
    plt.savefig(output_path)
    print(f"Scatter plot for 3 groups created and saved as {output_path}")

if __name__ == '__main__':
    main()
