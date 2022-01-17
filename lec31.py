'''
Exercise 6: Game Development: Snake Water Gun | Python Tutorials For Absolute Beginners In Hindi #40

'''
# import random
#
# name=input("Enter your name !")
# n=0 #for no of turns
# cu=0 # for user win
# cp=0 # for comp win
#
# while n<5:
#     choose=input("Please type your choice:\n"
#                    "1.Rock\n2.Paper\n3.Scissor\n")
#     L=["Rock","Paper","Scissor"]
#     comp=random.choice(L)
#     if choose == "Rock":
#         if comp == choose:
#             print(f"The Match Is draw::{choose}vs{comp}")
#         elif comp == "Scissor":
#             print(f"You Win ::{choose}vs{comp} ")
#             cu+=1
#         elif comp == "Paper":
#             print(f"You Lose :: {choose}vs{comp}")
#             cp+=1
#     if choose == "Paper":
#         if comp == choose:
#             print(f"The match is Draw :: {choose}vs{comp}")
#         elif comp == "Rock":
#             print(f"You win::{choose}vs{comp}")
#             cu+=1
#         elif comp == "Scissor":
#             print(f"You lose::{choose}vs{comp}")
#             cp+=1
#     if choose == "Scissor":
#         if comp == choose:
#             print(f"The Match is Draw ::{choose}vs{comp}")
#         elif comp == "Rock":
#             print(f"You Win::{choose}vs{comp}")
#             cu+=1
#         elif comp == "Paper":
#             print(f"You Lose :: {choose}vs{comp}")
#             cp+=1
#     n+=1
# if(cu>cp):
#     print(f"\n {name} is the Winner".upper())
# else:
#     print("\n Sorry Computer is the Winner ".upper())


"""This is a game of rock paper scissor using random module"""
import random
name=input("Please Enter your name")
n=0 #counter for number of games
cu=0#counter for wins of user
cp=0#counter for wins of computer
while n<5:
    choose=input("Please type your choice:\n"
               "1.Rock\n2.Paper\n3.Scissor")
    L=["Rock","Paper","Scissor"]
    comp=random.choice(L)
    if choose == "Rock":
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
        elif comp == "Rock":
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
