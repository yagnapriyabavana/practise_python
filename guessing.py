import random
name=input("enter your name:")
print(f'Hiii {name}! welcome to this game! This is a number guessing name \n Computer generates a number you need to guess the number ')
choice=7
sum=1
num=random.randint(1,100)
while sum<choice:
    guess=int(input("enter your choice"))
    if guess==num:
        print(f'great !!!! you did it correct in {sum} chances')
        break
    elif guess > num:
        print("the number is greater! plz enter a small  number ")
        sum=sum+1
    elif guess<num:
        print("the number is smaller! plz enter a greater number ")
        sum=sum+1
    else:
        print("please enter a valid number")
if num!=guess
    print(f'The number is {num}')
    print("Better Luck next time")