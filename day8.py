# -------------- First class exercise: --------------


# # Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     exact_can_number = (height * width) / coverage
#     number_of_cans = math.ceil(exact_can_number)
#     print(f"You'll need {number_of_cans} cans of paint.")

# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# -------------- Second class exercise: --------------


# # Write your code below this line 👇
# def prime_checker(number):
#     its_prime_number = False
#     placeholder = 0
#     for numbers_to_check in range(2, number):
#         if number % numbers_to_check > 0:
#             # print(f"It's not a prime number. (Checked {number}/{numbers_to_check})")
#             placeholder = 1
#         else:
#             # print(f"It's a prime number.(Checked {number}/{numbers_to_check})")
#             its_prime_number = True

#     if its_prime_number == True:
#         print(f"It's not a prime number.")
#     else:
#         print(f"It's a prime number.")


# # Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input()) # Check this number
# prime_checker(number=n)



# -------------- Homework exercise: --------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encoded_word = []
    for char in text:
        letter_index = alphabet.index(char)
        shifted_index = letter_index + shift
        encoded_word.append(alphabet[shifted_index])
        
        
    joined_encoded_word = ''.join(encoded_word)
    return joined_encoded_word

        
        
        
encripted_word = encrypt(text=text, shift=shift)
print(encripted_word)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in 
    # the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to 
# test the code and encrypt a message. 


