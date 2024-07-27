# For Question , Any Inquiry and Suggestion about the Program Contact me (chauhanrushil45@gmail.com)

# Rock Paper Scissors game

from random import *

l=["Rock","Paper","Scissors"]
rock = 1
paper = 2
scissors = 3
yourPoint = 0
computerPoint = 0

round = int(input("\nEnter the number of Rounds you want to play in ODD (1,3,5...) : "))
print("\n")
if round % 2 != 0:
    print('''
        NOTE : if your choice is invalid then one point will be deducted so play carefully
''')
    for i in range(1,round+1):
        print("\nRound :",i)
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player = int(input("Enter your choice(1,2,3): "))
        computer = randint(1,3)
        if player == computer:
            print("\nYour choice is :",l[player-1])
            print("Computer choice is :",l[computer-1])
            print("\nDraw")
            print("\nYour point is :",yourPoint)
            print("Computer point is :",computerPoint)
        elif player == rock and computer == scissors or player == paper and computer == rock or player == scissors and computer == paper:
            print("\nYour choice is :",l[player-1])
            print("Computer choice is :",l[computer-1])
            print("\nYou win")
            yourPoint = yourPoint + 1
            print("\nYour point is :",yourPoint)
            print("Computer point is :",computerPoint)
        elif computer == rock and player == scissors or computer == paper and player == rock or computer == scissors and player == paper:
            print("\nYour choice is :",l[player-1])
            print("Computer choice is :",l[computer-1])
            print("\nComputer wins")
            computerPoint = computerPoint + 1
            print("\nYour point is :",yourPoint)
            print("Computer point is :",computerPoint)
        else:
            print("\nInvalid choice")
            print("Your one point is deducted")
            yourPoint -= 1

    if yourPoint > computerPoint:
        print("\nYou win the game\n")
    elif yourPoint < computerPoint:
        print("\nComputer wins the game\n")
    else:
        print("\nGame is tie\n")
            
else:
    print("\nInvalid number of rounds\n")