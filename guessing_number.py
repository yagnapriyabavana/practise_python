import random
name=input("Enter your name:")
print(f"Hiii {name} Welcome to this game.\n This is a number guessing game you have got 7 chances to guess the number.Lets start the game")
number=random.randrange(100)
chances=7
guess_counter=0
while guess_counter < chances:
    guess_counter+=1
    my_guess=int(input("Enter a number you guess:"))
    if my_guess==number:
        print(f"the number is {number} and you found it right!! in the {guess_counter} attempt")
        break
    elif guess_counter>=chances and my_guess!=number:
        print(f"oops sorry,the number is   {number}  better luck next time")
        break
    elif my_guess>number:
        print("your guess is higher")
    elif my_guess<number:
        print("your guess is lesser")
