"""
Experiment Number: 28
File Name: experiment_28.py
Description: Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    
    plt.figure(figsize=(8, 6))
    plt.barh(languages, popularity, color='red')
    
    plt.xlabel('Popularity (%)')
    plt.ylabel('Languages')
    plt.title('Popularity of Programming Languages (Horizontal Bar Chart)\nWorldwide, Oct 2017 compared to a year ago')
    
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    
    plt.tight_layout()
    output_path = 'outputs/experiment_28_output.png'
    plt.savefig(output_path)
    print(f"Horizontal bar chart created and saved as {output_path}")

if __name__ == '__main__':
    main()
