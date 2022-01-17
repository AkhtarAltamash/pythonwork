"""
Map, Filter & Reduce | Python Tutorials For Absolute Beginners In Hindi #48
"""

number=["23","45","67"]
number = list(map(int,number))
# for i in range(len(number)): # dono sa same hi kam ho raha per hum loop ka ziada use nahi  karna ha
#     number[i]=int(number[i])

number[2]=number[2]+1
print(number[2])
