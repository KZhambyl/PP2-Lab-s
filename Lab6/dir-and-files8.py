# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def deleteByPath(path):
    os.remove(path)

path = input("Your path: ")
if (os.path.exists(path)):
    deleteByPath(path)
else: print("Path isn't exists.")