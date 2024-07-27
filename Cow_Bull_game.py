# For Question , Any Inquiry and Suggestion about the Program Contact me (chauhanrushil45@gmail.com)

# COW BULL GAME for Guessing 4 Digit Number 

import random #for generate a random number

def generate_random_number():
    digits = list(range(10))
    random.shuffle(digits)
    # Ensure the first digit is not 0 to maintain 4-digit number
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0] 
    return ''.join(map(str, digits[:4]))

number = str(generate_random_number())
Total_attemps = 0

print("\n\nRule : - 4 DIGIT NUMBER ONLY WITH NO REPEATED DIGITS\n\n")

while True:
    # Get user input
    guess = input("Guess a 4-digit number:- ")
    Total_attemps += 1
    bulls = 0
    cows = 0

# Check the user's guess
    
    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1 #if User's guess is correct Bull=Bull+1

        elif guess[i] in number:
            cows += 1 #if User's guess the number and the number is in number cow=cow+1
    
    # print after evrey guess that help to guess number in right direction to user
    print("Bulls:", bulls)
    print("Cows:", cows)
    if bulls == 4:
        print("Congratulations! You guessed the number correctly.")
        print("The number was", number)
        break
    elif Total_attemps == 20:
        print("Sorry, you ran out of guesses. The number was", number)
        break

if(Total_attemps<5):
    print("You're Gineous!")
    
print("You guessed the number in", Total_attemps, "attempts.") 
