import random

name = input("Hello! What is your name?\n")
num=random.randint(0,20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
quesses=0
on=True
while(on):
    answer=int(input("Take a quess.\n"))
    quesses+=1
    if answer==num:
        print(f"\nGood job, KBTU! You guessed my number in {quesses} guesses!")
        on=False
    elif answer < num:
        print("\nYour guess is too low.")
    else:
        print("\nYour guess is too large.")

