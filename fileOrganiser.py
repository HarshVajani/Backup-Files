import os
import shutil
path = input("Enter the name of the directory to get sorted")
list_of_files = os.listdir(path)
for file in list_of_files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
        