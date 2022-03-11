print("Number guessing game")
print("Guess a number between(1 to 7)")

guess= int (input("enter the number"))
if(guess<3):
    print("your guess was too low: Guess a number higher then 3")
elif(guess<4):
    print("your guess was too low: Guess a number higher then 4")
elif(guess<7):
    print("your guess was too low: Guess a number higher then 7")
else :
    print("Congratulation YOU WON!!")