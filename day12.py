# ################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # local Scope


# ################### HW project ####################

import random


def random_number():
    number = 0
    numbers_list = []
    for _ in range(100):
        number += 1
        numbers_list.append(number)
    random_number = random.choice(numbers_list)
    return random_number


def intro():
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("You have made a typing mistake...")
    return attempts


def game(guesses_left, number):
    while guesses_left > 0:
        print(f"You have {guesses_left} attepts remaining to guess the number.")
        guess = int(input("Make a guess. "))
        if guess > number:
            print("Too high.")
            guesses_left -= 1
        elif guess < number:
            print("Too low.")
            guesses_left -= 1
        else:
            print("You have WOOOOOOOON!")
            return
    print("You have lost the game.")


remaining_guesses = intro()
guessing_target_number = random_number()
game(guesses_left=remaining_guesses, number=guessing_target_number)
