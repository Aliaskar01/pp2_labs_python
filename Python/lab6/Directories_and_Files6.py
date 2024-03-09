import os

folder_path = r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab6\alphabet'
for a in range(26):
    b = chr(65+a)
    file_name = b+'.txt'
    full_path = os.path.join(folder_path, file_name)

    with open(full_path, 'w') as file:
        file.write("this file name is ")
        file.write(b)
        file.write(".txt")