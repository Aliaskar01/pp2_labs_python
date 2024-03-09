import os

path = r'C:\Users\alias\OneDrive\Рабочий стол\pp1'

for dirs, folders, files in os.walk(path):
    print(dirs)
    print(folders)
    print(files)