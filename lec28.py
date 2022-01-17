'''
Anonymous / lambda functions  # 1 line function bhi kaha jata ha
'''
#
# def add(x,y):
#     return x+y
# minus = lambda x,y:x-y # bus yeh faida ha ka def nahi kia
# print(minus(5,6))
'''
sort
'''
def a_first(a):
    return a[1]

a=[[110,40],[9,5],[2,23]]
a.sort(key=a_first)  # key ka word function layta ha or jis hisb sa ap ko sort karna ho
print(a)