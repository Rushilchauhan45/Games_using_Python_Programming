# For Question , Any Inquiry and Suggestion about the Program Contact me (chauhanrushil45@gmail.com)

# number guessing game between 1-100 (User have 15 chances to guess the number)

from random import *  # for random number generation

number = randint(1, 100)
count = 0

while True:
    
    x = int(input("\nGuess the number between 1 to 100 :- "))
    count += 1
    if count == 15:
        print("\nYou have out of chances")
        print("\nThe number was :", number)
        print("\nBetter luck next time\n")
        break
    if x == number:
        print("\nYou won the game. Congratulation")
        print("\nYou guessed it right in", count, "guesses\n")
        break
    elif x<number:
        print("Your guess is TOO LOW")
    elif x>number:
        print("Your guess is TOO HIGH")
    else:
        print("Invalid input")

if count == 5:
    print("\nYou're Genius\n")

