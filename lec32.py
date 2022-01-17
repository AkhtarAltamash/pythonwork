'''
*args and **kwargs In Python | Python Tutorials For Absolute Beginners In Hindi #41

# '''
# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("Altamash","ali" ,"akhtar","Ahmed") # jitna declare ha utny hi aeay ga

def funargs(normal,*args):                    # fiada ha ka jitna bhi name add kardo atay rahay ga masla nahi ho ga
    print(normal)
    for item in args:
        print(item)

har=["Altamash","ali" ,"akhtar","Ahmed"]
normal=345
funargs(normal,*har)
'''
hamesha pehla normal aeay ga phir arg aeay ga or phir last ma kwargs aeay ga 
'''
"""

# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)
  

"""