"""
Experiment Number: 29
File Name: experiment_29.py
Description: Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']
    
    plt.figure(figsize=(8, 6))
    plt.bar(languages, popularity, color=colors)
    
    plt.xlabel('Languages')
    plt.ylabel('Popularity (%)')
    plt.title('Popularity of Programming Languages with Custom Colors\nWorldwide, Oct 2017 compared to a year ago')
    
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    
    plt.tight_layout()
    output_path = 'outputs/experiment_29_output.png'
    plt.savefig(output_path)
    print(f"Bar chart with different colors created and saved as {output_path}")

if __name__ == '__main__':
    main()
