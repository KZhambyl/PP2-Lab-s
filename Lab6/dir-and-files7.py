text = ["Veni, Vidi, Vici!", "Memento Mori!", "Senatus Populusque Romanus", "Alea jacta est!"]
with open('firstText.txt','w')as f:
    for line in text:
        f.write(line+'\n')

# copy
    
with open('firstText.txt','r') as ff, open('copiedText.txt','w') as sf:
    for line in ff:
        sf.write(line)

