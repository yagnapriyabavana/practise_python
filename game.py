import random
print("Hii!!...This is a game of rock paper and  scissor.Your opponent will be computer.\n Rock  vs paper :winner is Paper \n Rock vs Scissors :winner is Rock \n paper vs scissors :winner is Scissors ")
while True:
    print("Enter your choice \n 1:Rock \n 2:paper \n3:Scissors")
    choice=int(input("Enter your choice:"))
    while choice > 3 or choice < 1:
        choice=int(input("Enter a valis choice:"))
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissors'
    print(f"your choice is : {choice_name}")
    print("It's computer turn:")
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissors'
    print(f"Computer choice is: {comp_choice}")
    print(choice_name,'vs',comp_choice_name)
    if choice_name==comp_choice_name:
        result="Draw"
    elif(choice==1 and comp_choice==2) or (comp_choice==1 and choice==2):
        result='Paper'
    elif(choice==1 and comp_choice==3) or(comp_choice==1 and choice==3):
        result='Rock'
    elif(choice==2 and comp_choice==3) or (comp_choice==2 and chance==3):
        result='Scissors'
    if result=="Draw":
        print("It's a tie")
    elif result==choice_name:
        print("User Wins")
    else:
        print("Computer Wins")
    print("Do you want to play this game again???(y/n)")
    ans=input().lower()
    if ans=='n':
        break
print("Thanks for playing!!!!")
