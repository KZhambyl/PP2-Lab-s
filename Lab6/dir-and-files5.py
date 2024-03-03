myList = ["Generation War", "Peaky Blinders", "True Detective", "Game of Thrones", "Band of Brothers"]

with open('Serials.txt','w') as file:
    for serial in myList:
        file.write(serial+'\n')

