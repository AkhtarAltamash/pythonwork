bankbalance=10000
print("*WELCOME TO ABC BANK* ")
pincode=int(input("Please Enter Your Pin Code : "))
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
    # s = input("enter the account no")
    if len(x) == 4:
        print("okk")
    else:
        print("wrong input")
        return 0

    print("Enter The Account Number In You Want To Transfer The Money")
    acc = int(input())

    z=bankbalance-acc
    if acc>bankbalance :
        print("*unsufficent Balance*")
    elif acc<bankbalance and acc<6000:
        print("please wait ")
        print("The Amount Is Transfer Successfully To \n The Account Number Is ",x ,"\n And The Remaining Amount Is ",z )
    else:
        print("The Amount Is Unvalid/ Can't transfer More Then 6000")

def billing():
    print("please wait ")
    print("select any one for the billing \n1* Electricity Bill \n2* Gas Bill \n3* Water Bill")
    a = int(input())
    if a == 1:
        Electricity()



    elif a == 2:
        GasBill()



    elif a == 3:
        WaterBill()

def Electricity():
            print("electricity")
            # print()
            e = input(" Enter the Bill No:")
            if len(e) == 4:
                print("okk")
            else:
                print("wrong input")
                return 0
            input(" Please mention your Address number: ")

            print("Successfully paid")

def GasBill():
            print(" Gas Bill")
            # print("electricity")
            # print()
            g = input(" Enter the Bill No:")
            if len(g) == 4:
                print("okk")
            else:
                print("wrong input")
                return 0
            input(" Please mention your Address number: ")

            print("Successfully paid")
def WaterBill():
            print(" Water Bill")
            # print("electricity")
            # print()
            w = input(" Enter the Bill No:")
            if len(w) == 4:
                print("okk")
            else:
                print("wrong input")
                return 0
            input(" Please mention your Address number: ")
            print("Successfully paid")





if pin == pincode:
    print("Pin Code Is Valid")
    print("Which Operation Do You Want To Perform 1 or 2 \n1* Withdraw \n2* Transfer \n3* Online Banking")
    choose = int(input())
    if choose == 2:
        transfer()


    if choose == 1:
         withdraw()

    if choose == 3:
        billing()

else:
    print("The Pin code Is Invalid")

