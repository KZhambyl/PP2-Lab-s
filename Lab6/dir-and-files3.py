import os

path = input("Path: ")
if(os.path.exists(path)):
    print("File name of the path:")
    print(os.path.basename(path))
    print("Directory name of the path:")
    print(os.path.dirname(path))
else: print("Path is not exists.")