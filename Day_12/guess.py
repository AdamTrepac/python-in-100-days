"""
Higher or lower guessing game:

Easy mode or hard mode == number of guesses

Pick a random number
Have user guess a number
Check if they are higher or lower

"""
import random
from art_guess import logo

print(logo)
number = random.randint(1,100)
game_over = False
print("I'm thinking of a number between 1 and 100 (inclusive), can you guess it?")
if input("Chose a difficulty, 'easy' or 'hard': ").lower() == "easy":
    attempts = 10
else:
    attempts = 5

while game_over == False:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    
    if guess == number:
        print("You guessed the correct number! You win!")
        break
    
    attempts -= 1
    if attempts < 1:
        game_over = True
        print("You ran out of guesses, the number was:", number)
        break

    if guess > number:
        print("Too high, guess again")
    else:
        print("Too low, guess again")
    








