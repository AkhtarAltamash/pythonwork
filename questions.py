

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

act_cost=500
sale_in=int(input("In how much you sale it : "))
rem=sale_in - act_cost

if sale_in > act_cost:
    print("You sale it in profit with:",rem)
elif sale_in < act_cost:
    print("You sale it in loss",rem)
elif sale_in == act_cost: 
    print(" You sale it in its actual price ",rem)
