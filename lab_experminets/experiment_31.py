"""
Experiment Number: 31
File Name: experiment_31.py
Description: Write a Python program to create a stacked bar plot with error bars. Note: Use bottom to stack the women's bars on top of the men's bars.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    groups = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = (22, 30, 35, 35, 26)
    women_means = (25, 32, 30, 35, 29)
    men_std = (4, 3, 4, 1, 5)
    women_std = (3, 5, 2, 3, 3)
    
    ind = np.arange(len(groups))
    width = 0.35
    
    plt.figure(figsize=(9, 6))
    p1 = plt.bar(ind, men_means, width, yerr=men_std, color='red', capsize=5, label='Men')
    p2 = plt.bar(ind, women_means, width, bottom=men_means, yerr=women_std, color='green', capsize=5, label='Women')
    
    plt.ylabel('Scores')
    plt.xlabel('Groups')
    plt.title('Scores by group and gender (Stacked with Error Bars)')
    plt.xticks(ind, groups)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    output_path = 'outputs/experiment_31_output.png'
    plt.savefig(output_path)
    print(f"Stacked bar plot with error bars created and saved as {output_path}")

if __name__ == '__main__':
    main()
