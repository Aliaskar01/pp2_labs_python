import os

file1 = r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab6\alphabet\A.txt'
file2 = r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab6\alphabet\Y.txt'

with open(file1, 'r') as f:
    file = f.read()

with open(file2, 'w') as f:
    f.write(file)