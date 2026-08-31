"""
Experiment Number: 23
File Name: experiment_23.py
Description: Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    x = []
    y = []
    
    with open('test.txt', 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
                
    print("Coordinates read from test.txt:")
    for xi, yi in zip(x, y):
        print(f"X: {xi}, Y: {yi}")
        
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue', marker='o')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Sample graph from text file!')
    plt.grid(True)
    plt.tight_layout()
    
    output_path = 'outputs/experiment_23_output.png'
    plt.savefig(output_path)
    print(f"Line plot created and saved as {output_path}")

if __name__ == '__main__':
    main()
