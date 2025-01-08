import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print(" We have selected a number between 1 and 100. Can you guess it?")
    
    numbertoguess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            userguess = int(input("Enter your guess: "))
            attempts += 1
            
            if userguess < numbertoguess:
                print("Too low! Try again.")
            elif userguess > numbertoguess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")
guess_the_number()