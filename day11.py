############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
from day11_art import logo

# to create a local clear_screen function()
import os
import platform


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
pc_cards = []

start_new_game_flag = False


# clear screen function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Unix/Linux/MacOS


def deal_card():
    random_card = random.choice(cards)
    return random_card


def game_start_card_draw():
    player_cards = []
    pc_cards = []
    for i in range(0, 2):
        player_cards.append(deal_card())
        pc_cards.append(deal_card())
    return player_cards, pc_cards


def calculate_cards_score(list_or_cards):
    hand_total = 0
    for card in list_or_cards:
        hand_total += card
    return hand_total


def check_for_blackjack(score):
    if score == 21:
        # print(f"******check_for_blackjack    Score: {score}")
        # print("******Blackjack check True")
        return "Blackjack"
    else:
        # print(f"********check_for_blackjack    Score: {score}")
        # print("******Blackjack check False")
        return "None"


def check_for_over21(score):
    if score > 21:
        # print(f"******check_for_over21 score: {score}")
        # print("******Over 21 True")
        return "Over21"
    else:
        # print(f"******check_for_over21 score: {score}")
        # print("******Over 21 False")
        return "None"


def check_for_ace(cards_list):
    # print(f"***** check_for_ace - old card list {cards_list}")
    for card in cards_list:
        if card == 11:
            card = 1
    # print(f"***** check_for_ace - new card list {cards_list}")
    return cards_list


def new_game():
    play_or_not_input = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    )
    user_cards, computer_cards = game_start_card_draw()
    if play_or_not_input == "y":
        start_new_game_flag = True
        clear_screen()
        print(logo)
        game(user_cards, computer_cards)
    else:
        start_new_game_flag = False


def game(player_cards, pc_cards):
    user_cards_score = calculate_cards_score(player_cards)
    computer_cards_score = calculate_cards_score(pc_cards)

    print(f" Your cards: {player_cards}, current score: {user_cards_score}")
    print(f" Computer's first card: {pc_cards[0]}")
    # print(f" [Computers full score {computer_cards_score} and cards {pc_cards}]")

    if check_for_blackjack(user_cards_score) == "Blackjack":
        if check_for_blackjack(computer_cards_score) == "Blackjack":
            print("You and Dealer has Blackjack! You lost...")
            new_game()
        else:
            print("Blackjack! You WON")
            new_game()
    elif check_for_blackjack(computer_cards_score) == "Blackjack":
        print("Dealer has Blackjack! You lost...")
        new_game()
    else:
        if check_for_over21(user_cards_score) == "Over21":
            check_for_ace(player_cards)
            if check_for_over21(user_cards_score) == "Over21":
                print(f"Player's score is over 21. You lost...")
                new_game()
        else:
            addition_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if addition_card == "y":
                player_cards.append(deal_card())
                user_cards_score = calculate_cards_score(player_cards)
                # print(f" Your cards: {player_cards}, current score: {user_cards_score}")
                # print(f" Computer's first card: {pc_cards[0]}")
                game(player_cards, pc_cards)
            elif addition_card == "n":
                while computer_cards_score < 17:
                    # print(computer_cards_score)
                    pc_cards.append(deal_card())
                    computer_cards_score = calculate_cards_score(pc_cards)
                    # print(pc_cards)
                if check_for_over21(computer_cards_score) == "Over21":
                    print(f"PC's score is over 21. You WON!")
                    new_game()
                else:
                    if user_cards_score > computer_cards_score:
                        print(
                            f"Your final hand {player_cards}, final score: {user_cards_score}."
                        )
                        print(
                            f"Computer's final hand {pc_cards}, final score: {computer_cards_score}."
                        )
                        print(f"Your score is higher. You WON!")
                        new_game()
                    elif user_cards_score < computer_cards_score:
                        print(
                            f"Your final hand {player_cards}, final score: {user_cards_score}."
                        )
                        print(
                            f"Computer's final hand {pc_cards}, final score: {computer_cards_score}."
                        )
                        print(f"Computer's score is higher. You lost.")
                        new_game()
                    else:
                        print(
                            f"Your final hand {player_cards}, final score: {user_cards_score}."
                        )
                        print(
                            f"Computer's final hand {pc_cards}, final score: {computer_cards_score}."
                        )
                        print(f"Score is equal. Its a draw...")
                        new_game()


new_game()
