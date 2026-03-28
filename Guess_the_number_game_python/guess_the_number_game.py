#guess the number game
#concepts used:while loo and user input.
#sample run:
#guess a number between 1 and 10:4
#wrong guess!Try again.
#guess again: 7
#Congratulations! You guessed it right.
import random
number_to_guess = random.randint(1, 10)
user_guess = None
while user_guess != number_to_guess:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
