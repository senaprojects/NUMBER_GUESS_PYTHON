
import random
num =random.randrange(1,100)
guess=int(input("Guess the number : "))
while(guess!=num):
    if(guess<num):
        print("You guess lower nnumber.choose higher!!")
        guess=int(input("\n Guess the number : "))
    else:            
        print("You guess higher number.choose lower!!")
        guess=int(input("\n Guess the number : "))
print("you guess the correct number!!.")
