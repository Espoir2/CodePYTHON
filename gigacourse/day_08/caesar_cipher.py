print("""
                                                                                                                                                          
  ,ad8888ba,                                                          ,ad8888ba,  88                         88                                 
 d8"'    `"8b                                                        d8"'    `"8b ""                         88                                 
d8'                                                                 d8'                                      88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba, 88            88 8b,dPPYba,  8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8 88            88 88P'    "8a 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88         Y8,           88 88       d8 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          Y8a.    .a8P 88 88b,   ,a8" 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88           `"Y8888Y"'  88 88`YbbdP"'  88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                     88          88                                             
                                                                                     88          88                                             



          """)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction_possibilities = ["encode", "decode"]


def caesar_cipher(the_message, the_shift, the_direction):
    
    end_message = ""
    if the_direction == "decode":
        the_shift *= -1
    for char in the_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + the_shift) % 26
            new_letter = alphabet[new_position]
            end_message += new_letter
        else:
            end_message += char
    print(f"The {the_direction}d text is : {end_message}")


should_continue = True
while should_continue:
    
    check = False
    while not check:
        direction = input("Type 'encode' to encode your message end 'decode' to decode it :\n ")
        if direction in direction_possibilities:
            check = True
    message = input("Type your message : \n ").lower()
    shift_str = ""
    while not shift_str.isdigit():
        shift_str = input("Type the shift number : \n ")
    shift = int(shift_str)

    caesar_cipher(the_message=message, the_shift=shift, the_direction=direction)


    check_02 = False
    while not check_02:
        ask_continue = input("Do you want to continue ? Type 'yes' if you want. Otherwise type 'no' \n ")
        if ask_continue in ['yes', 'no']:
            check_02 = True

    if ask_continue == 'no':
        should_continue = False
        print("Goodbye🖐")

# Todo_list
# 🔴 Print the caesar_cipher logo at the start of code






# Try of combine the two function
"""def caesar_cipher(the_message, the_shift, the_direction):
    if the_direction == "encode":
        cipher_message = ""
        for letter in the_message:
            position = alphabet.index(letter)
            new_position = (position + the_shift) % 26
            new_letter = alphabet[new_position]
            cipher_message += new_letter
        print(f"The encode text is : {cipher_message}")
    else:
        decrypted_message = ""
        for letter in the_message:
            position = alphabet.index(letter)
            new_position = (position - the_shift) % 26
            new_letter = alphabet[new_position]
            decrypted_message += new_letter
        print(f"The decode message is : {decrypted_message}")


caesar_cipher(the_message=message, the_shift=shift, the_direction=direction)"""
# my_trying
""""
message = list("abc")
shift = 1
print(message)
for position_alphabet in range(0, len(alphabet)):
    letter = alphabet[position_alphabet]
    print(position_alphabet, letter)
    if letter in "abc":
        print("letter in message")
        for position_message in range(len(message)):
            message_letter = message[position_message]
            print(position_message, message_letter)
            if letter == message_letter:
                message[position_message] = alphabet[position_alphabet + shift]
                alphabet.pop(position_alphabet+shift)
    print("-"*50)
print(message)
"""
