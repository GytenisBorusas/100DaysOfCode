import random


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


display = []

#creates empty list for the lenght of the random word with "_" for each letter
for _ in chosen_word:
    display += "_"
print(display)


guess = input("Guess a letter: ").lower()


position = 0
#checks if the guest letter is in the word
for letter in chosen_word:
    if letter == guess:
        display[position] = letter
        position += 1
    else:
        position += 1



print(display)
