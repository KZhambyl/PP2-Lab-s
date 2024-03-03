alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alp:
    with open(letter+'.txt', 'w') as file:
        file.write("")