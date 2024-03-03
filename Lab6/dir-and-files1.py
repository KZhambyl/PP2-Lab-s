import os

print("Directories:")
for file in os.scandir("Lab6"):
    if file.is_dir():
        print(file.name)

print("Directories and files:")
for file in os.scandir("Lab6"):
    print(file.name)

print("Files:")
for file in os.scandir("Lab6"):
    if file.is_file():
        print(file.name)