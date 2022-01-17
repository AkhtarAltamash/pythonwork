bankbalance=10000
print("*WELCOME TO ABC BANK* ")
pincode=int(input("Please Enter Your Pin Code"))
pin = 1234

def withdraw():
    print(" wait please with draw session ")
    print("Enter The Amount You Want To WithDraw")
    y=int(input())
    if y>bankbalance:
        print("Unsufficent Balance")
    else:
        print("Withdraw session Completed And The Amount Is ", y)

def transfer():
    print("Please wait while your transaction is being prosed ")
    print("Enter The Account No:")
    x=input()
    print("Enter The Account Number In You Want To Transfer The Money")
    acc = int(input())
    # l = l
    z=bankbalance-acc
    if acc>bankbalance :
        print("*unsufficent Balance*")
    elif acc<bankbalance and acc<6000:
        print("please wait ")
        print("The Amount Is Transfer Successfully To \n The Account Number Is ",x ,"\n And The Remaining Amount Is ",z )
    else:
        print("The Amount Is Unvalid/ Can't transfer More Then 6000")




if pin == pincode:
    print("Pin Code Is Valid")
    print("Which Operation Do You Want To Perform 1 or 2 \n1* Withdraw \n2* Transfer")
    choose = int(input())
    if choose == 2:
        transfer()


    if choose == 1:

        withdraw()

else:
    print("The Pin code Is Invalid")


# def withdraw(self):
#         amount = float(input("Enter amount to be withdrawn: "))
#         if self.balance >= amount:
#             self.balance -= amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
