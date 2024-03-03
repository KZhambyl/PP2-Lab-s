text = ["Line-1","Line-2","Line-3","Line-4","Line-5"]
#importing text to new file
with open('myFile.txt', 'w') as file:
    for line in text:
        file.write(line+"\n")

# counting number of lines
with open('myFile.txt', 'r') as file:
    lines = file.readlines()
print(f"The number of lines: {len(lines)}")