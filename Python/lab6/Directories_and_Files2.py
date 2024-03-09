import os

path_dir = input()
if os.path.exists(path_dir):
    print('exist')
    if os.access(path_dir, os.R_OK):
        print('readbale')
    else:
        print('not readbale')
    if os.access(path_dir, os.W_OK):
        print('writable')
    else:
        print('not writable')
    if os.access(path_dir, os.X_OK):
        print('executable')
    else:
        print('not executable')
else:
    print('not exist')