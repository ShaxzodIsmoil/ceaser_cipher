"""
DATE: 03/10/2021
Made by Shaxzodbek Rafiqov
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            new_char = char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet) - 1:
                new_position -= len(alphabet)
            elif new_position < 0:
                new_position += len(alphabet)
            new_char = alphabet[new_position]
        end_text += new_char
    print(f"Here's the {cipher_direction}d result: {end_text}")
    user = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if user == "yes":
        shifrlash()
    else:
        print("Hayr")


def shifrlash():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= len(alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


shifrlash()
