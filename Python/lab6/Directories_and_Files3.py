import os

path_dir = input()

if os.path.exists(path_dir):
    filename = input()
    for dirs, folders, files in os.walk(path_dir):
        if filename in files:
            file_path = os.path.join(dirs, filename)
            print("File find in:", file_path)

else:
    print("path doesn't exist")