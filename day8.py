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
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = []
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text.append(alphabet[new_position])
        
    joined_encoded_word = ''.join(cipher_text)
    print(f'The encoded text is "{joined_encoded_word}"')

def decrypt(cipher_text, shift_amount):
    deciphered_text = []
    reversed_alphabet = alphabet[::-1]
    for letter in cipher_text:
        position = reversed_alphabet.index(letter)
        new_position = position + shift_amount
        deciphered_text.append(reversed_alphabet[new_position])
        
    joined_decrypted_word = ''.join(deciphered_text)
    print(f'The decoded text is "{joined_decrypted_word}"')

if direction == "encode":
    encripted_word = encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decripted_word = decrypt(cipher_text=text, shift_amount=shift)
else:
    print("You can't type...")






#TODO-3: Check if the user wanted to encrypt or decrypt the message 
# by checking the 'direction' variable. Then call the correct function 
# based on that 'drection' variable. You should be able to test the 
# code to encrypt *AND* decrypt a message.
