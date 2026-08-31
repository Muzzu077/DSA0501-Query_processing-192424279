"""
Experiment Number: 35
File Name: experiment_35.py
Description: Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    plt.figure(figsize=(9, 6))
    plt.scatter(marks_range, math_marks, label='Math marks', color='red', marker='o')
    plt.scatter(marks_range, science_marks, label='Science marks', color='blue', marker='s')
    
    plt.title('Scatter Plot: Mathematics vs Science Marks')
    plt.xlabel('Marks Range')
    plt.ylabel('Marks Scored')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_35_output.png'
    plt.savefig(output_path)
    print(f"Scatter plot comparing subject marks created and saved as {output_path}")

if __name__ == '__main__':
    main()
