import os

file_path = input()

if os.path.exists(file_path):
    print("this file exist")
    if os.access(file_path, os.X_OK):
        print("this file executable")
        try:
            os.remove(file_path)
            print("this file deleted")
        except:
            print("we couldn't delete this file")
    else:
        print("this file doesn't executable")
else:
    print("this file doesn't exist")