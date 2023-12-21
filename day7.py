import random
from hangman_art import logo, stages 
from hangman_words import word_list


chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)

display = []

#creates empty list for the lenght of the random word with "_" for each letter
for _ in chosen_word:
    display += "_"

guessed_letter_list = []
lives = 6

while ("_" in display) and (lives > 0):
    print(stages[lives])
    print(f"{' '.join(display)}\n")
    print(f"You have {lives} lives left.")
    if len(guessed_letter_list) > 0:
        print(f"You have already tried [{' '.join(guessed_letter_list)}] letter(s).\n")
    guess = input("Guess a letter: ").lower()
       
    if guess in guessed_letter_list:
        print(f'You have already guessed "{guess}" before. Try a different letter.')
    else:
        guessed_letter_list.append(guess)
        

        life_lost_flag = True
        position = 0
        
        
        #checks if the guest letter is in the word
        for letter in chosen_word:
            if letter == guess:
                display[position] = letter
                position += 1
                life_lost_flag = False
            else:
                position += 1
                
        
        if life_lost_flag == True:
            print(f'Letter {guess} is not in the word.')
            lives -= 1
            
        
if lives == 0:
    print(stages[0])
    print("You are deaaaad!")
else:
    print(" ")
    print("***************************")
    print("You just WOOOOON!")
    print("***************************")
            
    
    
    
    
     
    



 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current 
 # umber of 'lives' the user has remaining.


