import random

my_list = ["rock","paper","scissior"]
computer_score = 0
user_score = 0
print("-"*41)
print("="*15,"Play Game","="*15)
print("-"*41)

for i in range(0,10):

    print("\n1. rock")
    print("2. paper")
    print("3. scissor")

    user_choice = int(input("Enter your Choice : "))
    comp_choice = random.choice(my_list)
    print("-"*27)
    print("| User Choice     : ",my_list[user_choice-1],"|")
    print("| Computer_Choice : ",comp_choice,"|")
    

    if(user_choice==1):
        if(comp_choice == "scissior"):
            user_score+=1
            print("| Result          : You Win |")
        elif(comp_choice == "paper"):
            computer_score+=1
            print("you lost")
        elif(comp_choice == "rock"):
            print("tie")

    elif(user_choice==2):
            if(comp_choice == "rock"):
                user_score+=1
                print("you win")
            elif(comp_choice == "scissior"):
                computer_score+=1
                print("you lost")
            elif(comp_choice == "paper"):
                print("tie")

    elif(user_choice==3):
            if(comp_choice == "paper"):
                user_score+=1
                print("you win")
            elif(comp_choice == "rock"):
                computer_score+=1
                print("you lost")
            elif(comp_choice == "scissior"):
                print("tie")

    else:
        print("Please Enter Valid Choice !!")

    print("-"*27)

    print("-------Score-------")
    print("| You      :",user_score,"   |")
    print("| Computer :",computer_score,"   |")
    print("-------------------")


    print("="*40)


if(user_score > computer_score):
    print("*"*20,"You Are win a Game","*"*20)
elif(user_score<computer_score):
    print("*"*20,"You Lost a Game","*"*20)
else:
    print("*"*20,"Match Draw","*"*20)

"""
rock  rock  tie
      paper lost
      scissior win

paper  rock  win
      paper tie
      scissior lost

scissior  rock  lost
          paper win
          scissior tie


"""
