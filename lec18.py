'''
LECTURE #18
'''
'''
i=0

while(True):
    if i+1 <5:
        i=i+1
        continue
    print(i+1, end=" ")
    if (i==40):
        break
    i = i + 1
    '''
'''
QUIZ
'''
'''
while(1):

    print("Enter Any Number \n")
    a = int(input())

    if (a >= 100):
        print("congrats")
        break
    else:
        continue
'''
'''
Exercise
'''
b=0
# as number of guess

while(b<5):

      print("Enter any number for guess")
      a = int(input())
      if ( a==20 ) :
          print("You are Correct congrats")
          break
      elif ( a>20 and a<=25):
          print("you are very close little down")


      elif (a >25):
        print("you are far MORE DOWN")

      elif (a < 20 and a > 15):
        print("you are very close little up")

      elif (a<15):
          print("you are far MORE UP ")
      else:
         # print("you won\n")
          #print(number_of_guesses, "no.of guesses he took to finish.")
          break
      print( 4- b, "no. of guesses left")
      b = b + 1

if (b > 4):
    print("Game Over")
