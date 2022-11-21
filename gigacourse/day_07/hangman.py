from random import *

# from rep-lit import clear

print("""
                WELCOME TO MY HANGMAN GAME

| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
               
""")

stages = [
    """
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / *
     |
    _|___
    """,
    """
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    """,

    """
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    """,

    """
        _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
    """,

    """
        _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    """,

    """
        _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
    """

]

word_list = ['coding', 'computer', 'work']
lives = 6
chosen_word = choice(word_list)
print(chosen_word)
display = ["_" for _ in range(len(chosen_word))]
print(display)


def print_list(the_list):
    for element in the_list:
        print(element, end=" ")


# while "_" in display: (My method)
end_game = False
while not end_game:
    user_letter = input("Guess et letter : ").lower()
    # clear()
    if user_letter in display:
        print(f"{user_letter} ?", end="   ")
        print("❎YOU ALREADY GUESS THIS LETTER ❎")

    if user_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_letter:
                display[position] = letter
    else:
        lives -= 1
        print("⛔ SORRY, THIS LETTER IS NOT IN THE WORD ⛔. YOU LOOSE A LIFE 💔")
        print(lives)
        print(stages[lives])
        # if lives == 5:
        #     print(stages[-1])
        # elif lives == 4:
        #     print(stages[-2])
        # elif lives == 3:
        #     print(stages[-3])
        # elif lives == 2:
        #     print(stages[-4])
        # elif lives == 1:
        #     print(stages[-5])

    print_list(display)
    print()
    if lives == 0:
        # print(stages[-6])
        end_game = True
        print(f"YOU LOOSE 😛. The answer is {chosen_word}")
    elif "_" not in display:
        end_game = True
        print("YOU WIN 🏆")

# Note_book
"""
Step_01 : 
🔷 Create a word list
🔷 Chosen a word in the word list
🔷 Get the user letter

Step_02 : 
🔷 Create the variable display that contains the dashes that wil be replace by the good letter guessed by the user 
🔷 For each good letter guessed by the user, replace the dash that is in it's position in display by the letter
🔷 Print display

Step_03 : 
🔷 Use while loop to permit to user to guess letter until display contain dash to permit him to win the game

Step_04 : 
🔷 Create a variable lives that equals to 6 
🔷 Make the lives reduce of 1 if the user guess a letter that is not in chosen word and make the game stop if lives equals to O 
🔷 Print the ASCII art for each stages

Step_05 : 
🔷 Replace the word list by the hangman word list
🔷 Import the logo of hangman at the start of the game
🔷 Import the stages of hangman ascii art
🔷 Manage the case where the user guess a letter that he already guess 
🔷 Let the user know if the letter that he guess is not in the chosen word
"""

# 01 My trying
"""
word_input = "coding"
word = list("coding")
word_len = len(word)
print(word)
letter = "c"


if letter in word:
    other_letters = word.pop()
    print(other_letters)
    #for j in other_letters:
        #new_word = word.replace(j, " ")

#print(new_word)
"""

# 02 Another trying

"""
word_list = ['coding', 'computer', 'work']

chosen_word = choice(word_list)
print(chosen_word)

user_letter = input("Guess et letter : ").lower()
find = []
c = 0
while c < len(chosen_word):
    user_letter = input("Guess et letter : ").lower()
    for i in chosen_word:
        if i == user_letter:
            print(i, end="")
            find.append(i)
        else:
            print("_", end="")
    c += 1

if len(find) < len(chosen_word):
    print("YOU LOOSE")
else:
    print("YOU WIN")
"""
