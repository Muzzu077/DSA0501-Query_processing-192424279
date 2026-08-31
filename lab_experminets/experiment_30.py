"""
Experiment Number: 30
File Name: experiment_30.py
Description: Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    groups = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = (22, 30, 35, 35, 26)
    women_means = (25, 32, 30, 35, 29)
    
    n_groups = len(groups)
    index = np.arange(n_groups)
    bar_width = 0.35
    
    plt.figure(figsize=(9, 6))
    plt.bar(index, men_means, bar_width, color='green', label='Men')
    plt.bar(index + bar_width, women_means, bar_width, color='red', label='Women')
    
    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by person and gender')
    plt.xticks(index + bar_width / 2, groups)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    output_path = 'outputs/experiment_30_output.png'
    plt.savefig(output_path)
    print(f"Grouped bar plot created and saved as {output_path}")

if __name__ == '__main__':
    main()
