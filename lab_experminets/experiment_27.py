"""
Experiment Number: 27
File Name: experiment_27.py
Description: Write a Python programming to display a bar chart of the popularity of programming Languages.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    
    plt.figure(figsize=(8, 6))
    plt.bar(languages, popularity, color='blue')
    
    plt.xlabel('Languages')
    plt.ylabel('Popularity (%)')
    plt.title('Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago')
    
    # Adding grid
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    
    plt.tight_layout()
    output_path = 'outputs/experiment_27_output.png'
    plt.savefig(output_path)
    print(f"Bar chart created and saved as {output_path}")

if __name__ == '__main__':
    main()
