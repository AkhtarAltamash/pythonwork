

# a = 30
# b= "muhammad altamash"
# c = 4.56
# d=True

# print(a)
# print(b)
# print(c)
# print(d)
# print( type(a))

# print("hello")

# print("The Value of 3+4 IS",3+4)

# a= "34343"
# a=int(a)
# print(type(a))1

# a= int( input("enter any number"))
# print(a)
# print(type(a))
# a= int(input("Enter any value"))
# z= int(input("enter another value"))
# print(a%z)

# a=input("entyer the value")
# print(type(a))
# a= 34
# b=80
# print(a>b)
# a=int(input("Enter vale for the average"))
# b=int(input("Enter vale for the average"))
# print((a+b)/2)

# a=int(input("ENTER THE VALUE FOR SQUARE ROOT : "))
# print(a*a)

# slicing python string

# greeting ="Good Morning"
# name ="Altamash"
# print( greeting + name)

# name ="altamash"
# print(name[4])
# print(name[1:6])
# print(name[-6:-1])
# print(name[1:8:2])
# story="reading stories is a great way to improve your vocabulary and we have lots of great stories for you to watch. Watch stories, print activities and post comments!"

# print(len(story))
# print(story.endswith("you"))
# print(story.count("a"))
# print(story.capitalize())

# print(story.find("you"))

# print(story.replace("you","yposad"))

# greeting="Good Morning , "
# a=input("Enter Your Name : ")
# print(greeting +a)

# letter='''Dear <|Name|>,
# You are selected !

# Date: <|Date|>'''


# name=input("Enter Your Name : \n")
# date =input("Enter Date : \n")
# letter=letter.replace("<|Name|>", name)
# letter=letter.replace("<|Date|>", date)

# print(letter)
# stri="This Is A String With Double   Spaces     "
# # print(stri.find("  "))
# print(stri.replace("   "," "))

# letter="Dear Harry, This Python Course Is Nice . Thanks !"

# Format_letter="Dear Harry\n\t, This Python Course Is Nice \n. Thanks !"
# print(Format_letter)

# create a list using []
# value  change kar sakta ha( can change the value) 
# a=[12,34,45,2,345,6,34]
# a[0]=21
# print(a)

# we can create a list with items of different types
# matlb aesa bhi kar skta ha 
# c=[4,"harry", False,6.9]

# friends=["Altamash", " ali"," ahmed", "sam","rohan", 45]
# print(friends[0:5:2])

# l1= [12,43,12,3,2,6,7,6,90]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.append(23) # last ak value add kardyta ha 
# print(l1)
# l1.insert(0,8)
# print(l1)
# l1.pop(2)
# print(l1)
# l1.remove(12)
# print(l1)

# TUPLES
#creating tuple using ()
#cannot update the values of tuples

# t=(1,21,1,1,3,4,5)
# print(t[0])
# t[0]=12  nahi possible ha 
# print(t) 
# print(t.count(1))

# print(t.index(3))

# f1=input("enter fruite number 1")
# f2=input("enter fruite number 2")
# f3=input("enter fruite number 3")
# f4=input("enter fruite number 4")
# f5=input("enter fruite number 5")
# f6=input("enter fruite number 6")
# f7=input("enter fruite number 7")

# myFruitList=[f1,f2,f3,f4,f5,f6,f7]
# print(myFruitList)

# m1=input("enter the marks of stu1 : ")
# m2=input("enter the marks of stu2 : ")
# m3=input("enter the marks of stu3 : ")
# m4=input("enter the marks of stu4 : ")
# m5=input("enter the marks of stu5 : ")
# m6=input("enter the marks of stu6 : ")

# MyMarksList=[m1,m2,m3,m4,m5,m6]
# MyMarksList.sort()
# print(MyMarksList)

# t1=(23,67,65,66,89)
# t1[0]=12
# print(t1)
# a=[2,3,4,5,6]
# print(a[0]+a[1])
# print(sum(a))

# a=(7,0,8,0,0,9)
# print(a.count(0))

# DICTIONARY
# MyDict={
#     "quick":"flash is faster",
#     "super":"Supurman is super",
#     "bat":"bruce wane ",
#     "Marks": [1,2,3,4,5],
#     "AnotherDictionary":{'harry':'Player',
#                         'Altamash':'coder'},
#     "quick":'superman is quick',
#     1:2
                    
# }
# print(MyDict)
# print(MyDict['quick'])
# print(MyDict["Marks"])
# print(MyDict['Marks'])
#  Values change ho sakti ha 
# duplicates kesa nahi ho sakti
# MyDict['Marks']=[23,34,45,56]
# print(MyDict['Marks'])
# print(MyDict["quick"])
# some propertise
# print(MyDict.keys())
# print(list(MyDict.keys()))
# print(MyDict.values())
# print(MyDict.items())
# Update_Dic={
#     "Iron Man":"Avengers",
#     "Caption America":"The First Avenger"
# }
# MyDict.update(Update_Dic)
# print(MyDict)

# SETS
#  retures that it is a dic not set 
# a={}
# print(type(a))

# b=set()
# print(type(b))
# b.add(5)
# b.add(7)
# list ko set ma nmahi dal sakta ha[] 
#  per tuple ko dak sakta ha ()
# dictionary ko bhi nahi dak sakta {}
# b.add((4,5,6))
# print(b)
# print(len(b))
# b.remove(7)
# print(b)

# print(b.pop())

# MyDic={
#     "PANKHA":"Fan",
#     "Daba":"Box",
#     "AnyThing": "Kuch bhi"
# }
# print("Select from the following option : ",MyDic.keys())
# a=input("Enter the hindi word\n")
# # print("The Meaning is : " ,MyDic[a])
# print("The Meaning is : " ,MyDic.get(a))

# a=int (input("enter the number : "))
# b=int (input("enter the number : "))
# c=int (input("enter the number : "))
# d=int (input("enter the number : "))
# e=int (input("enter the number : "))
# f=int (input("enter the number : "))
# g=int (input("enter the number : "))
# h=int (input("enter the number : "))

# MySet={a,b,c,d,e,f,g,h}
# print(MySet)

# s={18,"18"}
# print(s)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))
# s={}
# print(type(s))
# a=set()
# print(type(a))

# Fav_Lang={}
# a=input("Enter your fav language : \n")
# b=input("Enter your fav language : \n")
# c=input("Enter your fav language : \n")
# d=input("Enter your fav language : \n")

# Fav_Lang["Amhed "]=a
# Fav_Lang["Ali "]=b
# Fav_Lang["waqar "]=c
# Fav_Lang["qasim "]=b
# print(Fav_Lang)


# a=20        
# if(a>20):
#     print(True)
# elif(a<20):
#     print(False)
# else:
#     print("May be")
# print("DONE")

# age=int(input("Enter your age: \n"))
# if(age>=18):
#     print("Yes")
# else:
#     print("NO")
# age = int(input("Enter Your Age : \n"))

# if age>30 and age<50:
#     print("You can work with us ")
# else :print("no")
# a= None

# if a is None:
#     print("HAHAHA")
# else: print("NO")

# a=[12,23,34,45]

# if 23 in a:
#     print("hn jee")
# else : print("NO")

# a= int ( input("Enter Any number : "))
# b= int ( input("Enter 2nd  number : "))
# c= int ( input("Enter 3rd number : "))
# d= int ( input("Enter 4th number : "))

# if (a>d):
#     f1=a
# else:
#     f1=d
# if(b>c):
#     f2=b
# else:
#     f2=c
# if(f1>f2):
#     print( str (f1),"IS Greater")
# else:
#     print(str(f2)  ,"Is The Greater")           

# sub1=int( input("ENTER THE 1 SUB MARKS : "))
# sub2=int( input("ENTER THE 2 SUB MARKS : "))
# sub3=int( input("ENTER THE 3 SUB MARKS : "))

# if( sub1<33 or sub2<33 or sub3<33):
#     print (" You Are Fail !!")

# elif (sub1+sub3+sub2 )/3 <40:
#     print("AB MARKS KAM HONY KI WAJA SA FAIL HA BHAII !!")
# else:
#     print("PASS !@!")

# text=input("Enter The Text : \n")
# spam=False
# if("make alot of money" in text):
#     spam=True
# elif("Buy now" in text):
#     spam=True
# elif("Han bhai" in text):
#     spam=True
# else:
#     spam=False

# if(spam):
#     print("Yes their is a spam")
# else:
#     print("no spam")

# UserName=input("Enter your name : ")

# if(len(UserName)>5):
#     print(" Greatter than 5 alphabets !")
# else :
#     print("Short Name !")

# MyList=["Altamash","Akhtar", "Muhammad"]

# if("altamash" in MyList):
#     print("YESS IT IS")
# else:
#     print("NO BHAII")    

# marks=int(input("Enter Your Marks : "))
# if(marks>=90 and marks<=100):
#     print("Ex")
# elif(marks>=70 and marks<=89) :
#     print("A")
# elif(marks>=50 and marks<=69):
#     print("Pass")
# else:
#     print("Fail")

# UserStr="My name Is MUhammad AlTaMash Akhtar AND I am Doing My BacheLors FRom IndUs UniVERSITY"
# a=UserStr.lower()
# if("altamash" in a):
#     print("YES It Is There IN The String !")
# else:
#     print("No bhaiiii")

# i=0
# while(i<10):
#     print("True" + str(i))
#     i=i+1
# print("Done")
# i=0
# while(i<=50):
#     print(i)
#     i=i+1

    
# fruits=['Banana','Watermellon','Graphs','Mango']

# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

# l=[1,7,8]
# for item in l:
#     print(item)
# i=0
# fruits=['Banana','Watermellon','Graphs','Mango']

# for items in fruits:
#     print(items)
    
# for i in range(1,9,2):
#     print(i)

# l=[1,7,9]
# for i in l:
#     print(i)
# else:
#     print("done")
# for i in range(10):
#     print(i)
# else:
#     print("This is inside of for ")

# for i in range(10):
#     print(i)
#     if i==5:
#         break
# else: 
#     print("THIS is inside else of for")

# for i in range(10):
#     if i ==5:
#         continue
#     print(i)

# i=4
# if i>0:
#     pass
# print("harry is good")

# num=int(input("Enter any value"))

# for i in range(1,11):
#     # print(str(num)+"X"+str(i)+"="+str(num*i))
#     print(f"{num} X {i} = {num*i}")

# l1=["Harry","Sochan","Sachin","rahul"]

# for name in l1:
#     if name.startswith("S"):
#         # print(f"Hello {name}")
#         print(" hello " + name)
# num=int(input("Enter any digit for table : "))
# i=1
# while(i<11):
#     print(f"{num} X {i} = {num*i}")
#     i=i+1

# num=int(input("enter any number"))
# prime =True
# for i in range(2,num):
#     if(num%i == 0):
#         prime=False
#         break
# if prime:
#     print("This Number is Prime ")
# else :
#      print("this number is not Prime")

# n= int( input( "Enter any number : "))
# sum1=0

# while(n>0):
#     sum1=sum1+n
#     n=n=1
# print(" THE SUM IS :",sum1)

# num = int(input("Enter any number : "))
# factoril=1
# for i in range(1,num+1):
#     factoril=factoril*i
# print("the factorial is", factoril)

# for i in range(4):
#     print("*"*(i+1))

# for i in range(5):
#     print("*"*(i+1))

# n=3
# for i in range(3):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i-1))

# n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")    
#     print(" " * (n-i-1))

# n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))

# num=int(input("Enter the number for table : "))

# for i in range(10,0,-1):
#     print(f"{num} x {i} = {num*i}")
# n=4
# for i in range(4,0,-1):
#     print("*"*i,end="")
#     print(" "*(n-i-1),end="")
#     print(" " *(n-i-1))

# *****************************************
#  function

# def percent(marks):
#     p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
#     return p

# marks1=[67,78,89,90]
# percent1=percent(marks1)

# marks2=[64,67,54,88]
# percent2=percent(marks2)

# print(percent1,percent2)

# def func1(name):
#     print("hELLO "+name)

# def sum(num1,num2):
#     return num1+num2

# func1("Altamash")
# s=sum(12,12)
# print(s)

# def greet(name="NO Name :"):
#     print("Hello good morning ", name)

# greet("Altamash")
# greet()
#  FACTORIAL
#  n!= 1*2*3*3*...n

# n=4
# product=1
# for i in range(4):
#     product=product* (i+1)

# print(product)

# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product* (i+1)
#     return product


# def factorial_recursive(n):

#         if n==1 or n==0:
#             return 1
#         return n*factorial_recursive(n-1)

# f=factorial_recursive(0)
# print(f)


# print(factorial_iter(5))

# def maximum(num1,num2,num3):
#     if num1>num2 :
#         if num1 > num3:
#             return num1
#         else : 
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else: return num3

# MaxNum=maximum(23,12,2)
# print(MaxNum)

# def maximum(num1,num2,num3):
#     if(num1 > num2 and num1 > num3):
#         return num1
#     elif(num2>num1 and num2>num3):
#         return num2
#     elif(num3>num1 and num3>num2):
#         return num3

# m=maximum(12,43,32)
# print(m)

# def Fera(celc):
#     return (celc *(9/5))+32
# F=Fera(16)
# print(F)

# def sumx(n):
#     if(n==0):
#         return 0;
#     return n+sumx(n-1)
# s=sumx(4)
# print(s)

# def Pat(n):

# n=3
# for i in range(n):
#     print("*" * (n-i))
# ****************************************************
##############GAME#########################

# import random

# def Gamewin(comp,you):
#     if comp == you:
#         return None
#     elif comp=='s':
#         if you=='w':
#             return False
#         elif you=='g':
#             return True
#     elif comp=='w':
#         if you=='g':
#             return False
#         elif you=='s':
#             return True
#     elif comp=='g':
#         if you=='s':
#             return False
#         elif you=='w':
#             return True



# print("Computer's Ture : Snake (s) Water (w) Gun (g)")
# randomNo=random.randint(1,3)

# if randomNo ==1:
#     comp ='s'
# elif randomNo ==2:
#     comp = 'w'
# elif randomNo ==3:
#     comp='g'

# you=input("Your's Ture : Snake (s) Water (w) Gun (g)")
# a= Gamewin(comp,you)

# print(f"Computer chose {comp}")
# print(f" You chosse {you}")
# if a == None:
#     print(" The game is tie")
# elif a:
#     print("You won ")
# else:print("you lose ")

# f=open("sample.txt","r")
# data=f.read()
# print(data)
# f.close()
# f=open("sample.txt","r")
# data=f.readline()
# print(data)
# f.close()
# ****************
# f=open("another.txt","w")
# f.write(" hi there My name is Muhammad Altamash Akhtar :")
# f.close
# f=open("another.txt","a")
# f.write(" I am Appending ")
# f.close

# with open('another.txt','r') as f:
#     a = f.read()
# print(a)
# *****************************

# f= open("poem.txt","r")
# data=f.read()
# print(data)
# if 'twinkle' in data:
#     print(" twinkel is present")
# else:print(" Not present")
# f.close
# **********
# def game():
#     return 32

# score=game()
# with open("hiscore.txt") as f:
#     hiscore = int(f.read())
# if hiscore <score:
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))

# def game():
#     return 644
# score=game()
# with open("hiscore.txt","r") as f:
#     hiscorestr= f.read()

# if hiscorestr=='':
#      with open("hiscore.txt","w") as f:
#         f.write(str(score))

# elif int(hiscorestr)<score :
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))
# 888888888888888888888888888888888888888888888


# for i in range(1,21):
#     with open(f"Table/Muiltiplication_table_of{i}",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j} = {i*j}")
#             if j!=10:
#                 f.write("\n")    

# for i in range(1,21):
#     with open(f"tables/Multiplication_of_Table_{i}",'w') as f:
#         for j in range(1,10):
#             f.write(f"{i} X {j} = {i*j}")
#             if j!=10:
#                 f.write("\n")
# ****************

# with open("sample.txt",'r') as f:
#     content=f.read()
# content=content.replace("donkey","######")

# with open("sample.txt",'w') as f:
#     f.write(content)

# words=["donkey",'kaddu',"motay"]
# with open("sample.txt",'r') as f:
#     content=f.read()
# for word in words:
#     content=content.replace(word,"######")

# with open("sample.txt",'w') as f:
#     f.write(content)

# # **************************************

# with open("log.txt") as f:
#     content = f.read().lower()

# if 'python ' in content :
#     print(" yes python is in contant")
# else : print(" No thier is no python :")

# 88888888888888888888


# content=True
# i=1
# with open("log.txt") as f:
#    while content:
#     content = f.readline()

#     if 'python ' in content :
#         print(content)
#         print(f" yes python is in contant {i}")
#         print(i)
#     i+=1
# ****************************
# with open("this.txt") as f:
#     content = f.read()

# with open("copy.txt",'w') as f:
#     f.write(content)

# 88888888888888888888888888

# with open("this.txt") as f:
#     f1=f.read()
# with open("copy.txt") as f:
#     f2=f.read()
# if f1 == f2 :
#     print(" yes the content is same")
# else : print (" The files are not same ")
# ---------------------------------
# with open("this.txt",'w') as f:
#     f.write(" ")
# # --------------------------
# import os
# with open("this.txt") as f:
#     content =f.read()

# with open("Renamed_by_Python",'w') as f:
#     f.write(content)

# os.remove("this.txt")
# **********************************************
# OOP

# class Employee:
#     def __init__(self,Fname,Lname,salary) :
#         self.fname=Fname
#         self.lname=Lname
#         self.salary=salary
        
#     pass

# harry =Employee('HarryBhai',"JaksonMa",100000)
# rohan =Employee('RohanNameHa','dASS',201000)

# # harry.Fname="Harry"
# # harry.Lname="Jakson"
# # harry.salary=10000
# # rohan.Fname="Rohan"
# # rohan.Lname="Dass"
# # rohan.salary=20000
# print(rohan.fname)
# print(harry.fname)

# class Teacher :
#     increment=1.5
#     def __init__(self,Tfname,Tlname,Tsalary,Tsubject) -> None:
#         pass
#         self.tfname=Tfname
#         self.tlname=Tlname
#         self.tsalary=Tsalary
#         self.subject=Tsubject
    
#     def increase(self):
#         self.tsalary=int(self.tsalary * Teacher.increment)


# Altamash=Teacher("Altamash","Akhtar",5000,"Computer")
# Aman=Teacher("Aman","Rahim",10000,"Chemistry")        

# # print(Aman.tfname,Aman.tlname)
# print(Altamash.tsalary)
# Altamash.increase()
# print(Altamash.tsalary)


# class Employee():
#     increment=1.5
#     def __init__(self,Fname,Lname,Salary) -> None:
#         pass
    
#         self.fname=Fname
#         self.lname=Lname
#         self.salary=Salary
#     def increase(self):
#         self.salary=int(self.salary * Employee.increment)
#         pass
#     @classmethod
#     def change_increment(cls,amount):
#         cls. increment=amount

# Altamash=Employee("Muhammad ","Altamash ", 2000)

# print(Altamash.fname)
# print(Altamash.salary)
# Altamash.increase()
# print(Altamash.salary)

# print(Altamash.salary)
# Employee.change_increment(2)
# Altamash.increase()
# print(Altamash.salary)

# class Programmer:
#     company="Microsoft"
#     def __init__(self,name,product) -> None:
#         self.name=name
#         self.product=product
#     def getinfo(self):
#         print(f"The name of the { self.company} programmer is {self.name} and the product is {self.product}")

# harry=Programmer("HARRY","SKYPE")
# Alka=Programmer("AlkaR","Github")
# harry.getinfo()

# class Calculator:
#     def __init__(self,num) -> None:
#         self.number =num
#     def Square(self):
#         print(f"The square of {self.number} is {self.number **2}")

#     def SquareRoot(self):
#         print(f"The square of {self.number} is {self.number ** 0.5}")


#     def cube(self):
#         print(f"The square of {self.number} is {self.number ** 3}")

# a=Calculator(3)
# a.Square()
# a.SquareRoot()
# a.cube()

# class sample:
#     a="Harry"

# obj=sample()
# obj.a="Vikkay"
# print(sample.a)
# sample.a="HN  BHAI"
# print(obj.a)
# print(sample.a)

# ****************?

# class Calculator:
#     def __init__(self,num) -> None:
#         self.number =num
#     def Square(self):
#         print(f"The square of {self.number} is {self.number **2}")

#     def SquareRoot(self):
#         print(f"The square of {self.number} is {self.number ** 0.5}")


#     def cube(self):
#         print(f"The square of {self.number} is {self.number ** 3}")

#     @staticmethod
#     def greet():
#         print("**********Hello there welcome to the world*********** ")

# a=Calculator(3)
# a.greet()
# a.Square()
# a.SquareRoot()
# a.cube()

# class Train:
#     def __init__(self,name,fare,seats) :
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#     def GetStatus(self):
#         print(f"The name of the train is : {self.name}")
#         print(f"The seats available of the train is : {self.seats}")
#     def FareInfo(self):
#         print(f"The price of the ticket is : {self.fare}")

#     def BookTicket(self):
#         if(self.seats>0):
#             print(f"Your ticket has been booked and seat no is {self.seats}")
#             self.seats=self.seats-1
#         else:
#             print(" no seats are available :")


# intercity=Train("Intercity Express :10120",90,2)
# intercity.GetStatus()
# intercity.FareInfo()
# intercity.BookTicket()
# intercity.GetStatus()

# ******************************

# class sample:
#     def __init__(harry,name) -> None:
#         harry.name=name

# obj=sample("harry12")
# print(obj.name)

# ************ SINGLE INHERITANCE ********************
# class Employee:
#     company="GOOGLE"

#     def showDetails(self):
#         print("this is an employee")

# class programmer(Employee):
    
#     language="Python"
#     company="Youtube"
#     def GetLang(self):
#         print(f"This language is {self.language}")

#     def showDetails(self):
#         print("This is an programmer ")


# e=Employee()

# e.showDetails()
# p=programmer()
# p.showDetails()
# p.GetLang()
# print(p.company)
# print(p.language)
# *******************multi inheritance ****************

# class Employee:
#     company="VISA"
#     ecode=1234

# class FreeLanceing:
#     company="FIVER"
#     Level= 1

#     def UpgradeLevel(self):
#         self.Level=self.Level +1

# class Programmer(FreeLanceing,Employee):
#     Name="Altamash"

# p=Programmer()
# print(p.company)
# print(p.Name)
# p.UpgradeLevel()
# print(p.Level)
# **************************** MULTI LEVEL ************************


# class Person:
#     contry="Pakistan"

#     def __init__(self) :
#         print(" Initiallizing Person @@@@@@ \n")


#     def takeBreath(self):
#         print(" I am Breathing .....")

# class Employee(Person):
#     company="Honda"

#     def __init__(self) :
#         super().__init__()
#         print(" Initiallizing Employee @@@@@@ \n")

#     def GetSalary(self):
#         print(f" My salary is heheh")
    
#     def takeBreath(self):
#         print("I am an Employee and I am Breathing ....")

# class Programmer(Employee):
#     company="Fiverr"

#     def __init__(self) :
#         # super().__init__()
#         print(" Initiallizing PRogrammer @@@@@@ \n")
    
#     def GetSalary(self):
#         print(f" NO salary To the Programmer !!!1 ")
    
#     def takeBreath(self):
#         super().takeBreath()
#         print("I am an Programmer and I am Breathing ++ ++ ++")


# p=Person()
# p.takeBreath()
# e=Employee()
# e.GetSalary()
# pr=Programmer()
# pr.takeBreath()

# e=Employee()
# pr=Programmer()

# class Employee :
#     company ="Camel"
#     location="Delhi"
#     salary=1200

#     @classmethod # aesa bhi kar sakta ha 
#     def changeSalary(cls,sal): #--> ak yeh tareeka ha 
#         cls.salary=sal

         # _____________PROPERTY | GETTERS________________
# class Employee:
#     def changeSalary(self,sal):
#         self.salary=sal
#         # self.salary=sal
#         # self.__class__.salary=sal # --> class ka instance ko change karna ak yeh tareeka ha 

# e=Employee()
# print(e.salary)
# e.changeSalary(45222)
# print(e.salary)
# print(Employee.salary)



# _________Operator Overloading__________


# ***************************

# class c2dVec:

#     def __init__(self,i,j) -> None:
#         self.icap=i
#         self.jcap=j

#     def __str__(self) -> str:
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(c2dVec):
#     def __init__(self, i, j, k) -> None:
#         super().__init__(i, j)
#         self.kcap=k

#     def __str__(self) -> str:
#         return f"{self.icap}i+ {self.jcap}j + {self.kcap}k"

# v2d=c2dVec(1,3)
# v3d=C3dVec(1,9,7)
# print(v2d)
# print(v3d)
# ***************************
# class Animal:
#     AnimalType="Mammal"

# class pet(Animal):
#     Color="White"

# class dog(pet):
#     @staticmethod
#     def Bark():
#         print("bhoou bhouu")

# D=dog()
# D.Bark()

# ****************************
# salaryAfterIncrement =salary*increment
# class Employee:
#     salary=2000
#     increment=1.5

#     @property
#     def SalaryAfterIncrement(self):
#         return self.salary*self.increment

#     @SalaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary

# e=Employee()
# print(e.salaryAfterIncrement)
# print(e.increment)
# e.salaryAfterIncrement=2000
# print(e.increment)

# ***********************

# class complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i

#     def __add__(self,c):
#         return complex(self.real + c.real, self.imaginary+c.imaginary)

#     def __mul__(self,c):
#         mulReal= self.real*c.real-self.imaginary*c.imaginary
#         return complex(self.real + c.real, self.imaginary+c.imaginary)

#     def __str__(self) -> str:
#         return f"{self.real} + {self.imaginary}i"

# c1=complex(1,9)
# c2=complex(4,8)

# print(c1+c2)

# ****************PROJECT*****************

# import random
# randNmub=random.randint(1,100)
# print(randNmub)
# guess=0
# UserGuess=None
# while(UserGuess != randNmub):

#     UserGuess=int(input("Enter The number For Your Guess !! "))
#     guess+=1

#     if (UserGuess==randNmub):
#         print("You Guessed it right *-* ")
#     else:
#         if(UserGuess>randNmub):
#             print("You Guessed It Wrong !'ENTER A SMALLER NUMBER' ")
#         else:
#             print("You Guessed It Wrong !'ENTER A LARGER NUMBER'")

# print(f"you guessed the number in {guess} guesses !!")

# with open("high_Score.txt",'r') as f:
#     high_Score=int(f.read())

# if(guess<high_Score):
#     print(" You Have Guess Broken the hi-Score !!")
#     with open("high_Score.txt",'w') as f:
#         f.write(str(guess))
# ***********##########***************#######

# try


# while(True):
#     print("Enter Q to quit the game")
#     a=input("Enter any number : ")
#     if a=='Q'or a=='q':
#         break
#     try:
#         a=int(a)
#         if a>6:
#             print("You enter a number greater then 6 :")
#     except Exception as e:
#         print(f"THE ERROR IS {e}")
        

# print(" THANKX for playing the game :")

# DIFFERENT EXCEPTIONS :-

# try:
#     a=int(input("Enter any number :"))
#     c=1/a
#     print(c)

# except ValueError as e:
#     print(" Please enter the valid value :")
#     print(e)

# except ZeroDivisionError as e:
#     print(" make sure you are not dividing by 0 :")

# print(" Thanks for using this code !!")

# # *****************
# try:
#     i=int(input("Enter any number : "))
#     c=1/i

# except Exception as E:
#     print(E)

# else :            # aesa tab hoga jab try to run hoga per error nahi hoga to wo direct else ka pass jayga
#     print("We were successfull")
# *****************
# try:
#     i=int(input("Enter any number : "))
#     c=1/i

# except Exception as E:
#     print(E)
#     exit()

# finally : # (for clean up) yeh ak aesi cheez ha jo apna karna hi karna ha chay error ho ya nahi ya pehly exit kardo bhaly
#     print("Finally we are Done ")
    
# print(" Thanks for using the program !") # error aeay ga to exception ka bad yeh run nahi hoga per finally hoga 



# def greet(Name):
#     print(f"Good Morning {Name}")

# if __name__ =="__main__":
    
#     n=(input("Enter a Name : \n"))
#     greet(n)

# ***************** global locals*************

# a=8  # Globle
# def fun1():
#     global a
#     print(a)
#     a=56 # local 
#     print(a)
# fun1()
# print(a)
# # *************** enumerate**********
# list1=[3,4,5,6,False,5.67,"Harry"]
# # index=0
# # for item in list1:
# #     print(item,index) # isay behtr nichy wala kar sakta ha emurate karka
# #     index+=1

# for index,item in enumerate (list1):
#     print(item,index)

# a=[3,4,5,6,7,85,7,6,78,6,77]
# b=[]
# ********************* List comprehention********
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# b=[i for i in a if i%2==0]
# print(b)
# s={i for i in a}
# print(s)

##############Problemsss#############33

# def readFile(filename):

#     try:
#         with open(filename,'r') as f:
#             print(f.read())

#     except FileNotFoundError:
#         print(f"File {filename} is not Found")

    
# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")

# ***********************************

# l=[1,2,3,4,5,6,7,8,9,10]
# for index,item in enumerate(l):
#     if index==2 or index==4 or index==6:
#         # print(index,item)
#         print(f"The {index +1}th element is {item} ")

# ************************

# num=int(input(" Enter Any number :"))
# table=[num *i for i in range(1,11)]
# print(table)

# a=int(input(" Enter number a : "))
# b=int(input("Enter number b : "))
# try:
#     print(a/b)
# except :
#     print("Infinite : ")

# ***********************
num=int(input(" Enter Any number :"))
table=[num *i for i in range(1,11)]
print(table)

with open("table.txt",'a') as f :
    f.write(str(table))
    f.write('\n')
