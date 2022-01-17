# l = 10 # global
#
# def function1(n):
#    # l=5 #local
#   # m=8    #local
#     global l
#     l = l + 45
#     print(l)
#     print(n,"i have printed")
#
# function1("this is me")
# #print(m)

x = 100
def harry():
    x=10
    def rohan():
        global x
        x=30
    print("BEFORE",x)
    rohan()
    print("AFTER",x)
    rohan()
harry()
print(x)