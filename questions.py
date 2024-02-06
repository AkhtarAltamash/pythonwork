

# numbers = [10, 5, 7, 15, 3]

# max_number = max(numbers)
# max_index = numbers.index(max_number)

# print("The greatest number is", max_number)
# print("Its index is", max_index)

# num1= int(input("Enter Any Number: "))
# # num2= int(input("Enter Any Number: "))

# if num1%2 == 0:
#     print("the number is even")
# else:
#     print("The number is Odd")


# pakistani=["Samosa","Biryani","Pulao"]
# chinese=["chickpop","egg roll","fried rice"]
# italian=["pizza","pasta","risotto"]

# dish=input("Enter any dish name")

# if dish in pakistani:
#     print("The dish is pakistani")
# elif dish in chinese:
#     print(" The dish is in chinese")
# elif dish in italian:
#     print(" the dish is Italian")
# else:
#     print("The dish is random")


# exp=[2457,125,7867,43457,326,44,6799,989]

# total=0

# for item in exp:
#     total=total+item

# print(f"the total is  {total}")
# print(type(total))

# def calculate_total(exp):
#     total=0
#     for item in exp:
#         total=total+item
#     return total

# tom_expenses_list=[200,300,400]
# joe_expenses_list=[400,500,600]

# tom_total=calculate_total(tom_expenses_list)
# joe_total=calculate_total(joe_expenses_list)

# print("tomes total:",tom_total)
# print("joe's total :",joe_total)
# ************************************************************************

# Question number 1

# a=int(input("Enter the first age : "))
# b=int(input("Enter the seccond age : "))
# c=int(input("Enter the third age : "))

# if a> b and c:
#     print(f"a= {a} is the greatest among all as b= {b} and c= {c}")


# if b> a and c:
#     print(f"b= {b} is the greatest among all as a= {a} and c= {c}")

# if c> a and b:
#     print(f"c= {c} is the greatest among all as a= {a} and b= {b}")
# max=a
# if max > b:
#     max=a
# elif max > c:
#     max=c
# print("the max is " ,max)

# QUESTION1 :User will input (3ages).Find the oldest one

# a = int(input("Enter the first age: "))
# b = int(input("Enter the second age: "))
# c = int(input("Enter the third age: "))

# max_age = a

# if b > max_age:
#     max_age = b

# if c > max_age:
#     max_age = c

# print("The maximum age is:", max_age)

# QUESTION 2 : Write a program that will convert celsius value to fahrenheit
# (°C × 9/5) + 32 = °F

# c= int(input("Enter temperature to convert in fahrenheit : "))

# F= (c * 9/5) + 32
# print(f"The temperature of celsius {c}* in fahrenheit is {F}")

# QUESTION 3 :User will input (2numbers).Write a program to swap the numbers

# a=int(input("Enter the 1st number : "))
# b= int(input(" Enter the 2nd number "))

# c=a
# a=b
# b=c


# print(f"After swaping {a} {b}")

# QUESTION 4: Write a program that will give you the sum of 3 digits

# a= int(input(" Enter any number :"))
# b= int(input(" Enter any number :"))
# c= int(input(" Enter any number :"))

# sum = a+b+c
# print("The sum is ", sum)

# num = int(input("Enter the three number digits : "))

# a=num % 10 #( % matlb module sa yeh hoga ka last ma jo bhi hoga sub ma sa ho denote hoga )
# num=num //10 # ( // sa last ka digit hat jay ha or remaining count hoga)
# b=num%10
# c=num //10

# sum=a+b+c
# print(sum)


# num= int(input("Enter the digits for the sum :"))

# a=num%10
# num=num//10
# b=num%10
# num=num//10
# c=num%10
# d=num//10

# rev=(a+b+c+d)
# print(rev)

# Question 5: Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# a=1234

# rev=

# number = int(input("Enter a number: "))

# reversed_number = int(str(number)[::-1])

# print("Reversed number:", reversed_number)


# string = "Hello, World!"
# reversed_string = string[::-1]
# print(reversed_string)  # Output: "!dlroW ,olleH"


# text="Altamash"
# rev_text=text[::-1]
# print(rev_text)

# num=int(input("Enter the number to reverse :"))

# rev_num=int(str(num)[::-1])
# print(rev_num)

# num=int(input("Enter the number to reverse :"))

# a=num %10
# num=num//10

# b=num%10
# num=num//10

# c=num%10
# d=num//10

# rev=1000*a + 100*b +10*c + d
# print(rev)

# Question 6: Write a program that will tell whether the number entered by the user is odd or even.


# a=int(input("Enter any number to find out weather it is odd or even :"))

# if a%2==0:
#     print(f"{a} number is an even number! ")
# else:
#     print(f"{a} number is an Odd number !!")

# Question 7: Write a program that will tell whether the given year is a leap year or not.

# year=int(input("Enter any year to check it is leap year or not : "))

# if year%4 == 0:
#     print(f"{year} Yes it is a leap year !! ") 
# else:
#     print(f"{year} no it is not a leap year !")

# QUESTION 8 :Write a program to find the euclidean distance between two coordinates.

# x_1=float(input("Enter x1 of x cordinate : "))
# x_2=float(input("Enter x2 of x cordinate : "))
# y_1=float(input("Enter y1 of y cordinate : "))
# y_2=float(input("Enter y2 of y cordinate : "))

# d= ((x_2 - x_1)**2 + (y_2 - y_1)**2 )**0.5
# print(d)

# QUESTION 9 :Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

# a=int(input("Enter the 1st angle: "))
# b=int(input("Enter the 2nd angle: "))
# c=int(input("Enter the 3rd angle: "))

# if (a+b+c) == 180 and a!=0 and b!=0 and c!=0:
#     print(f"Yes it can make a triangle : {a}+{b}+{c} : it makes 180*") 
# else:
#     print("No it can make a triangle")

# QUESTION 10: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

# act_cost=500
# sale_in=int(input("In how much you sale it : "))
# rem=sale_in - act_cost

# if sale_in > act_cost:
#     print("You sale it in profit with:",rem)
# elif sale_in < act_cost:
#     print("You sale it in loss",rem)
# elif sale_in == act_cost: 
#     print(" You sale it in its actual price ",rem)

# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))

# if a>b:
#     print(f"A is graeter then B where a is {a} and b is {b} ")
# elif b>a:
#     print(f"B is graeter then A where a is {a} and b is {b} ")
# else: print(f"They both are same equal a is {a} and b is {b}")

# SQUARE * CODE
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print(" ")

#  INCREASING SQUARE
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# Decreas SQUARE
# num=5
# for i in range(num):
#     for j in range(i,num):
#         print("*", end="")
#     print("")

# Right Side triangle

# num=5

# for i in range(num):

#     for j in range(i,num):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# def my_func():
#     print(" This I s my function !!!! ")

# my_func()

# def details(email,password):
#     print(f"My email is {email} and my password is {password}")

# details("altamash@gmail.com","1234321")

# def factorial(n):
#     for i in range(n):
#         if n==0 or n==1:
#             return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# l1=[1,2,3,4,5]
# l2=[6,7,8,9]
# # l1.append(l2)    
# # print(l1)
# # print(len(l1))
# l1.extend(l2)
# print(l1)
# print(len(l1))

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Set up the Chrome WebDriver
# driver = webdriver.Chrome()

# # Open Google Maps
# driver.get("https://www.google.com/maps")

# # Find the search box and enter the place name you want to search for
# search_box = driver.find_element(By.ID, "searchboxinput")
# search_box.send_keys("kfc")

# # Find and click the search button
# search_button = driver.find_element(By.ID, "searchbox-searchbutton")
# search_button.click()

# # Find the "More Reviews" link and click it
# more_reviews_link = driver.find_element(By.LINK_TEXT, "More reviews")
# more_reviews_link.click()

# # Find all the review elements
# review_elements = driver.find_elements(By.CSS_SELECTOR, ".section-review-content")

# # Print each review
# for review_element in review_elements:
#     review_text = review_element.find_element(By.CSS_SELECTOR, ".section-review-text").text
#     print(review_text)

# # Close the browser
# driver.quit()


# from selenium import webdriver
# from bs4 import BeautifulSoup
# import re

# name = input("Enter Name: ")
# url = f"https://www.google.com/maps/search/{name}"

# # Set up the Chrome WebDriver (ensure you have chromedriver installed)
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')
# options.add_argument('--headless')  # To run Chrome in headless mode
# driver = webdriver.Chrome(options=options)

# driver.get(url)

# # Extract links from the page source after JavaScript rendering
# page_source = driver.page_source

# # Parse the page source with BeautifulSoup to extract links
# soup = BeautifulSoup(page_source, "html.parser")
# links = soup.find_all("a", href=True)

# # Convert extracted links to a list
# extracted_links = [link['href'] for link in links]

# driver.quit()

# # Define a regex pattern to match "branch" URLs (customize the pattern as per your requirement)
# branch_pattern = re.compile(r'^https://www.google.com/maps/place/.*')

# # Filter out URLs based on the specified pattern (keep only "branch" URLs)
# filtered_links = [link for link in extracted_links if branch_pattern.match(link)]

# print(filtered_links)


# name="Altamash"
# print(name)

# def a_name():
#     y=1
#     name="Akhtar"
#     print(name)
#     print(y)
# a_name()
# print(name)


# def generator():
#     for i in range(1000):
#         yield i
#         # print(i)

# g=generator()
# l1=[]
# for j in g:
#     l1.append(j)

# print(l1)

# def number_generator(n):
#     for i in range(n):
#         yield i

# # Create a generator that yields integers from 0 to 9
# my_generator = number_generator(10)

# # Initialize an empty list
# my_list = []

# # Append values from the generator to the list
# for value in my_generator:
#     my_list.append(value)

# # Print the resulting list
# print(my_list)


# def my_generator():
#     for i in range(100):
#         yield i
        
# g=my_generator()

# l1=[]

# for j in g:
#     l1.append(j)
# print(l1)


# arr=[-1,1,2,3,1]
# target=2

# for i in arr:
#     i=i+i
#     print(i)
#     if i == target:
#         print(i)
#         break
#     elif i<=target:
#         continue
#     else:
#         continue

# print(f"Number of target : {n}" )

# arr=[-1,1,2,3,1]
# target=2
# arr1=[]

# for i in arr:
#     for j in arr[1:]:
#         n=i+j

#     if n == target:
#         # print(n)
#         arr1.append(n)
#     elif n < target:
#         arr1.append(n)
#     else:
#         continue
# print(arr1)

# print(arr1.count(n))

# if __name__ == '__main__':
#     my_str="Hello, World"
#     print(my_str)

# a=int(input("Enter the 1st value you want to enter: "))
# b=int(input("Enter the 2nd value you want to enter: "))

# # a,b=b,a
# c=a
# a=b
# b=c

# print(f"The value of a is: {a}")
# print(f"The value of b is: {b}")

# num=int(input("Enter the 1st value you want to enter: "))

# if a%2 == 0 :
#     print("The number is even !")
# else: print("The number is odd !")

# n=int(input("Enter value you want to enter: "))
# flag=True

# if n<2:
#     flag=False
# else: True
    
# for i in range(2,n):
#     if n%i == 0:
#         flag =False

# if  flag == True:
#     print(n," Is a prime number :")
    
# else:
#     print(n, " is not a prime number :")


# n = int(input("Enter a number: "))
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{n} is a prime number.")
# else:
    # print(f"{n} is not a prime number.")

# num=int(input("Enter any number :"))
# def factorial(num):
#     if num == 0 or num==1:
#         return 1
#     elif num<0:
#         return "Not possible"
#     else:
#         return num * factorial(num-1)

# print(factorial(num))

# factorial =1
# num=-1

# if num<0:
#     print("Not possible")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"The factorial of {num}  is {factorial}")
# num=5
# def factorial(num):
#     return 1 if (num == 0 or num == 1)  else num*factorial(num-1) 
# print(factorial(num))

# n=10
# for i in range(1,n):
#     print(i)

# a=0
# b=1
# num=int(input("Enter the number :"))

# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,num+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# def faboRec(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return faboRec(n-1)+faboRec(n-2)
    
# print(faboRec(6))

# arr=[1,2,3,4,5,6,7]

# print(sum(arr))


# arr=[1,2,3,4,5,6,7]
# su=0
# for i in arr:
#     su = su + i
# print(su)

# l1=[]
# n=int(input("Enter the number: "))

# for i in range(0,n):
#     t=int(input("Enter value: "))
#     l1.append(t)

# su=0
# for i in l1:
#     su = su + i
# print(su)

# _________________MAZIMUM & MINIMUM________________



# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# max_value=arry[0]
# max_index=0

# for i in range(1,len(arry)):
#     if arry[i] > max_value:
#         max_value=arry[i]
#         max_index=i
# print("Maximum number in the array:", max_value)
# print("Maximum number index in the array is:", max_index)


# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# min_value=arry[0]
# min_index=0

# for i in range(1,len(arry)):
#     if arry[i] < min_value:
#         min_value=arry[i]
#         min_index=i
# print("Max value is :",min_value)
# print("Max index is :",min_index)

# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# count=0
# for i in arry:
#     count=count + 1
# print(count)

# _____test ___________

# arr=[-1,1,2,3,1]
# target=2
# arr1=[]

# for i in arr:
#     for j in arr[1:len(arr)]:
#         n=i+j

#     if n == target:
#         # print(n)
#         arr1.append(n)
#     elif n < target:
#         arr1.append(n)
#     else:
#         continue
# print(arr1)
# count=0
# for i in arr1:
#     count=count+1
# print(count)


# ___________swap first and last____________

# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# size=len(arry)

# temp=arry[0]
# arry[0]=arry[size-1]
# arry[size-1]=temp

# print(arry)

# arry = [23, 43, 12, 100, 5, 3, 55, 40]

# print("before" ,arry)

# tem=arry[0]
# arry[0]=arry[-1]
# arry[-1]=tem

# print("After" ,arry)
#_________________  swap any 2 _________

# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# print(arry)

# pos1,pos2=1,3
# arry[pos1],arry[pos2]=arry[pos2],arry[pos1]
# print(arry)
# ___________
# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# print("before",arry)
# pos1,pos2=1,3
# first_elem=arry.pop(pos1)
# second_elem=arry.pop(pos2)

# arry.insert(pos1,second_elem)
# arry.insert(pos2,first_elem)

# print("after" ,arry)
# ____________
# arry = [23, 43, 12, 100, 5, 3, 55, 40]
# print("Before :",arry)

# pos1,pos2=1,4
# get=(arry[pos1],arry[pos2])
# (arry[pos2],arry[pos1])=get
# print("after",arry)
# __________________ delete similar value______________-
# list=['geek','for','geek']
# word='geek'
# n=2
# cont=0
# for i in range(0,len(list)):
#     if list[i]==word:
#         cont=cont+1
#         if cont ==n:
#             del list[i]
# print(list)
# __________________________________
# list=['geek','for','geek']
# word='geek'
# cont=0
# times=2

# for i in range(0,len(list)):
#     if list[i] == word:
#         cont=cont+1
#         if cont == times:
#             del list[i]
# print(list)

# ______________search elemnt_______________
# list=[1,2,3,4,5,6,7,8]
# ele =9
# if ele in list:
#     print("element found")
# else:print("no found")

# list=[1,2,3,4,5,6,7,8]
# ele =7

# print("Element found" if ele in list else "Not found")


# list=[1,2,3,4,5,6,7,8]
# ele =5
# flag=0

# for i in list:
#     if i == ele:
#         print("Element found")
#         flag=1
#         break
# if (flag == 0):
#     print("Element not found")

# _________________clear a list______________

# list=[1,2,3,4,5,6,7,8]
# print("Before the list is :", list)

# list.clear()
# print("After the list is :", list )

# _______________reverse______
# list=[1,2,3,4,5,6,7,8]
# print("Before the list is :" , list)
# list.reverse()
# print("After the list is :", list)

# list=[1,2,3,4,5,6,7,8]
# print(list)
# list2=list[::-1]
# print(list2)

# list=[1,2,3,4,5,6,7,8]

# list2=list[::-1]
# print(list2)

# _______copy, clone list______

# list=[1,2,3,4,5,6,7,8]

# list2=list[:]
# print(list2)



# list2=[]
# list2.extend(list)
# print(list2)

# __________ count occurence of an element ______________

# list1=[1,2,3,4,6,3,5,6,8,5,8,99,0]
# occ=3
# cont=0

# for i in list1:
#     if i == occ:
#         cont= cont+1
# print(f"the number {occ} repeats {cont}")

# list1=[1,2,3,4,6,3,5,6,8,5,8,99,0]
# ele=3

# print("The element {} repeate {} times !".format(ele,list1.count(ele)))
# _____________________sum ________________
# list1=[1,2,3,4,6]
# cont=0

# for i in list1:
#     cont=cont+i

# print(cont)

#  __________ Multiply all numbers __________

# list1=[1,2,3,4,6]
# cont=1

# for i in list1:
#     cont=cont*i
# print(cont)
# import numpy as np

# list1=[1,2,3,4,6]
# result=np.prod(list1)
# print(result)

# _____________ smallest or largest_____

# list1=[12,43,1,82,3,45,4,6]

# list1.sort()

# print("The smallest is : ",list1[0] )
# print("The largest is : ",list1[-1])

# list1=[12,43,1,82,3,45,4,6]
# print("The smallest is: ",min(list1))
# print("The largest is: ",max(list1))
# _________________second largest__________

# list1=[12,43,1,82,3,45,4,6]
# list1.sort()

# print("The second largest is: ", list1[-2])

# ______________Reverse sentence___________

# sent="Welcome To Python Programming"

# word=sent.split()
# print(word)

# word=word[::-1]
# print(word)

# __________________ sub present or nor________
# sent="Welcome To Python Programming"

# if "Python" in sent:
#     print("yes")
# else:print("no")
# ____________count numbers______

# stri="akhtar"
# cont=0
# for i in stri:
#     cont=cont + 1
# print(cont)

# str="Altamash"

# print(len(str))

# ___________________
# def faboRec(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return faboRec(n-1)+faboRec(n-2)
    
    
# print(faboRec(7))

# def faboRec(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return faboRec(n-1)+faboRec(n-2)
# n=7
# fibo_ser =[faboRec(i) for i in range(n)]
# result=faboRec(n)
    
# print(f"Fibonacci series up to {n} terms: {fibo_ser}")
# print(f"The {n}-th Fibonacci number is: {result}")
# print(faboRec(7))

# _______JOIN_____

# lis=["john","Randy Ortan","CM Punk","Sheamus","Rock"]

# a=" and ".join(lis)
# print(a)



# _____________________

# def generator():
#     for i in range(1000):
#         yield i
#         # print(i)

# g=generator()
# l1=[]
# for j in g:
#     l1.append(j)

# print(l1)

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# # Create a generator
# my_generator = count_up_to(5)

# # Use the next function to retrieve the next value
# first_value = next(my_generator)
# print("First value:", first_value)

# # Use next again to get the next value
# second_value = next(my_generator)
# print("Second value:", second_value)

# # Alternatively, use a loop to iterate through the remaining values
# for num in my_generator:
#     print("Next value in the loop:", num)

# _________________
# def gen(num):
#     for i in range(num):
#         yield i

# g=gen(100)
# print("The First Value :",next(g))
# print("The second Value :",next(g))
# print("The third Value :",next(g))

# for j in g:
#     print("The loop value after :",j)
# ___________________



# def Common_Word():
#     sen1=input("Enter the 1 st word:")
#     sen2=input("Enter the 2 nd word:")

#     sen1=set(sen1)
#     sen2=set(sen2)
#     print(sen1)
#     print(sen2)

#     word_found=sen1 & sen2
#     print(word_found)
# Common_Word()

# ____________________ Binary one in another

# a = 5  # Binary representation: 0b0101
# b = 3  # Binary representation: 0b0011
#   & matlb intersection similar data ko print karta ha 
# result = a & b  # Binary result: 0b0001 (Decimal: 1)
# print(result)
 

# _________frequency of word appearing _______

# def frequence():
#     word=input("Enter the sentence for frequency: ")
#     lis=word.split()
#     d={}
    
#     for i in lis:
#         if i not in d.keys():
#             d[i]=1
#         else:
#             d[i] +=1
#     print(d)

# frequence()



# def convert():
#     Key=['Fahad','Mahad','Yasir']
#     values=[1235,5224,887765]

#     result=dict(zip(Key,values))
#     # print(result)
    
#     for i in result.items():
#         print(i)

# convert()


# __________________


#  Tuple ma sa remove ya pop ya drop nahi kar sakta per tuple ka ander list sa kar sakta ha 

# data=(1,"Danish Ali ",8.0,["Danish","Ali",29],"DK")
# data[3].pop()
# data[3].append("Master")
# data[3].remove("Danish")
# print(data)

# _________________________

# def sum(a,b,c):
#     return a+b+c


# c=10
# d=20
# e=20

# add=sum(c,d,e)
# print(add)
# ____________________

# def last_chr(a):
#     return a[-1]

# b=last_chr("Altamash")
# print(b)

# ____________________

#  MAP , FILTER AND REDUCTION _________

# def cube(x,y,z):
#     return x*y*z

# print(cube(2,3,6))

# def cube(x):
#     return x*x*x
# print(cube(3))


# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# for i in l:
#     l1.append(cube(i))
# print(l1)
    
# yeh same kam map sa bhi kar sakta ha 
# ____map_______
# def cube(x):
#     return x*x*x
# print(cube(3))
# l=[1,2,3,4,5,6,7,8,9]


# function or next kis per lagana 

# newl=list(map(cube,l))
# print(newl)
# ____filter_______
# same map ki terha use kary ga per 
# ak cheez jati ha or kam ki cheez nikal layta ha matlb jo qualify kary ga wo aea jay ga 

# def filter_func(x):
#     return x>4
# l=[1,2,3,4,5,6,7,8,9]

# nnewl=list(filter(filter_func,l))
# print(nnewl)

# ____Reduce_______

# sub ko output ma la kar jor dayta ha matlb sub ko reducekar ka ak kardyta ha 

# from functools import reduce

# numbers=[1,2,3,4,5]
#  map filter ya reduce kuch bhi ak terf(kia operation perform karna , kis per karna )
# sum=reduce(lambda x,y: x+y ,numbers)
# print(sum)

# ___________  ZIP___________________
# 2 cheezo ko jor dayga 

# data1=[1,2,3,4,5,6]
# data2=[6,5,4,3,2,1]
# data3=list(zip(data1,data2))
# print(data3)

#  ALL AND ANY FUNCTION:
# true ya false ma hi answer karta ha about condition
# odd=[1,3,5,7,9]
# even=[2,4,6,8]

# check=all([num % 2 == 0 for num in even])
# print(check)
# ______
# odd=[1,3,5,7,9,10]
# even=[2,4,6,8]

# check=any([num % 2 == 0 for num in odd])
# print(check)

# __________INHERITANCE__________________

# class Employee():
#     def __init__(self,name,id) -> None:
#         self.name = name
#         self.id = id
        
#     def showDetails(self):
#         print(f"The name of the Employess is {self.name} and id is {self.id}")
        
# class Developer(Employee):
#     def showLang(self):
#         print(f"The programmer is working on python")
          
# # e1=Employee("Altamash",711)
# # e1.showDetails()
# # e2=Employee("Akhtar",777)
# # e2.showDetails()
# e3=Developer("Muhammad",232)
# e3.showLang()
# __________________
# ___________single __________
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog:
    def bark(self):
        print("Dog barks")

class Fish(Animal,Dog):
    def swim(self):
        print("Fish swim")
    
fish=Fish()
fish.swim()
fish.bark()
fish.speak()
# Example usage
# dog = Dog()
# dog.speak()  # Inherited from Animal
# dog.bark()   # Defined in Dog

# ___________Multi_________
# class Flyable:
#     def fly(self):
#         print("Can fly")

# class Swimmable:
#     def swim(self):
#         print("Can swim")

# class FlyingFish(Flyable, Swimmable):
#     pass

# # Example usage
# flying_fish = FlyingFish()
# flying_fish.fly()
# flying_fish.swim()
