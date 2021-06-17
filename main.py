from art import logo
import random


def guess_game(n, guess, turns):
    if (n < guess):
        print("Too high")
        return turns - 1
    elif (n > guess):
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answer was {n}")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
easy_turns = 10
hard_turns = 5

if (level == 'easy'):
    turns = easy_turns
else:
    turns = hard_turns

ans = random.randint(1, 100)

guess = 0
while (guess != ans):
    print(f"You have {turns} attempts to guess a number.")
    guess = int(input("Make a guess: "))
    turns = guess_game(ans, guess, turns)
    if (turns == 0):
        print("You've run out of guesses. You lose.")
        break
    elif (guess != ans):
        print("Guess again")

# Project by Shivani Verma