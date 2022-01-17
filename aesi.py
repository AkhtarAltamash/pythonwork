

"""This is a game of rock paper scissor using random module"""
import random
name=input("Please Enter your name")
n=0 #counter for number of games
cu=0#counter for wins of user
cp=0#counter for wins of computer
while n<5:
    choose=input("Please type your choice:\n"
               "1.Rock =1 \n2.Paper = 2 \n3.Scissor = 3 ")
    L=[1,"Paper","Scissor"]
    comp=random.choice(L)
    if choose == 1:
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Scissor":
            print(f"You won ::{choose} vs {comp}")
            cu+=1
        elif comp == "Paper":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
    if choose == "Paper":
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Scissor":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
        elif comp == 1:
            print(f"You Won ::{choose} vs {comp}")
            cu+=1
    if choose == "Scissor":
        if comp == choose:
            print(f"Match is draw::{choose} vs {comp} ")
        elif comp == "Paper":
            print(f"You won ::{choose} vs {comp}")
            cu+=1
        elif comp == "Rock":
            print(f"You Lost ::{choose} vs {comp}")
            cp+=1
    n+=1
if(cu>cp):
    print(f"\n{name} is the Winner".upper())
elif(cu==cp):
    print(f"The Match is Draw Between:: {choose} vs {comp}")
else:
    print("\nSorry Computer is a winner".upper())



#
# print("hello")