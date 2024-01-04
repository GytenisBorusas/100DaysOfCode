import random
from day14_art import logo, vs
from day14_gamedata import data


# to create a local clear_screen function()
import os
import platform


# clear screen function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Unix/Linux/MacOS


def game():
    user_score = 0
    end_of_game_flag = False

    print(logo)
    random_entry_A = random.choice(data)
    print(
        f"Compare A: {random_entry_A['name']}, {random_entry_A['description']}, from {random_entry_A['country']}, "
    )
    print(f"****** {random_entry_A['follower_count']}")
    print(vs)
    random_entry_B = random.choice(data)
    print(
        f"Against B: {random_entry_B['name']}, {random_entry_B['description']}, from {random_entry_B['country']}, "
    )
    print(f"****** {random_entry_B['follower_count']}")

    while end_of_game_flag == False:
        users_input = input("Who has more followers? Type 'A' or 'B': ")

        if users_input == "A" and (
            random_entry_A["follower_count"] > random_entry_B["follower_count"]
        ):
            user_score += 1
            random_entry_A = random_entry_B
            clear_screen()

            print(logo)
            print(f"You're right! Current score: {user_score}")
            print(
                f"Compare A: {random_entry_A['name']}, {random_entry_A['description']}, from {random_entry_A['country']}, "
            )
            print(f"****** {random_entry_A['follower_count']}")
            print(vs)
            random_entry_B = random.choice(data)
            print(
                f"Against B: {random_entry_B['name']}, {random_entry_B['description']}, from {random_entry_B['country']}, "
            )
            print(f"****** {random_entry_B['follower_count']}")
            # users_input = input("Who has more followers? Type 'A' or 'B': ")

        elif users_input == "A" and (
            random_entry_A["follower_count"] < random_entry_B["follower_count"]
        ):
            end_of_game_flag = True
        elif users_input == "B" and (
            random_entry_A["follower_count"] > random_entry_B["follower_count"]
        ):
            end_of_game_flag = True
        elif users_input == "B" and (
            random_entry_A["follower_count"] < random_entry_B["follower_count"]
        ):
            user_score += 1
            random_entry_A = random_entry_B
            clear_screen()

            print(logo)
            print(f"You're right! Current score: {user_score}")
            print(
                f"Compare A: {random_entry_A['name']}, {random_entry_A['description']}, from {random_entry_A['country']}, "
            )
            print(f"****** {random_entry_A['follower_count']}")
            print(vs)
            random_entry_B = random.choice(data)
            print(
                f"Against B: {random_entry_B['name']}, {random_entry_B['description']}, from {random_entry_B['country']}, "
            )
            print(f"****** {random_entry_B['follower_count']}")
            # users_input = input("Who has more followers? Type 'A' or 'B': ")
        else:
            print(f"You mistyped something...")

    clear_screen()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {user_score}")


game()
