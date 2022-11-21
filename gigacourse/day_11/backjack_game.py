# import eslib

logo = """
                                                                                          
88888888ba  88                       88               88                       88         
88      "8b 88                       88               88                       88         
88      ,8P 88                       88               88                       88         
88aaaaaa8P' 88 ,adPPYYba,  ,adPPYba, 88   ,d8         88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88""""""8b, 88 ""     `Y8 a8"     "" 88 ,a8"          88 ""     `Y8 a8"     "" 88 ,a8"    
88      `8b 88 ,adPPPPP88 8b         8888[            88 ,adPPPPP88 8b         8888[      
88      a8P 88 88,    ,88 "8a,   ,aa 88`"Yba, 88,   ,d88 88,    ,88 "8a,   ,aa 88`"Yba,   
88888888P"  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a "Y8888P"  `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                                                          
                                                  
"""

def exact_str_input(possibilities, text="Type your answer : ", error_text="Please check your answer! Retry : "):
    answer = input(text).lower()
    if answer not in possibilities:
        while answer not in possibilities:
            answer = input(error_text)
    return answer
from random import *

def calc_computer_score():
    global computer_cards
    return sum(computer_cards)
    
def calc_user_score():
    global user_cards
    return sum(user_cards)


    

def print_stat(comp_cards, us_cards, comp_score, us_score, the_user_name):
    print(f"{'💥'*10} COMPUTER {'💥'*10}")
    print(f"Cards : {comp_cards} \t Curent score : {comp_score} ")
    print("-"*40)
    print(f"{'💥'*10} {the_user_name} {'💥'*10}")
    print(f"Cards : {us_cards} \t Curent score : {us_score} ")
    print("-"*40)
    print()


def has_backjack():
    global computer_score, user_score, is_game_over
    if computer_score == 21:
        print("Computer has a blackJack \t YOU LOOSE!😛")
        is_game_over = True
        return True
    elif user_score == 21:
        print("You have a blackJack. \t YOU WIN 🏆!!!")
        is_game_over = False
        return True
    else:
        # over_21()
        return False

def over_21():
    global user_score, computer_score
    if user_score <= 21:
        return False
    for position in range(len(user_cards)):
        card = user_cards[position]
        if card == 11:
            user_cards[position] = 1
        # else:
        #     print("Your score over 21. \t YOU LOOSE")
        #     return True
    new_user_score = calc_user_score()
    if new_user_score <= 21:
        print(" 🔄 Your score is over 21. Replacing your AS by 1 🔄")
        print_stat(comp_cards=computer_cards, us_cards=user_cards, comp_score=computer_score, us_score=new_user_score, the_user_name=name)

    if new_user_score <= 21:
        return False
    print("Your score over 21. \t YOU LOOSE! 😛")
    return True
    
def comp_over_21():
    return computer_score > 21
    


def ask_get_another_card():
    answer = exact_str_input(text=" ❓ Do you want to takes another cards? \t Type 'y' or 'n' : ",
                             possibilities=['y', 'n'])
    return answer == 'y'

def draw_another_card():
    global user_cards, cards
    user_cards.append(choice(cards))
    
def comp_new_card():
    global computer_cards, computer_score, cards
    computer_cards.append(choice(cards))
    computer_score = calc_computer_score()

def restart():
    answer = exact_str_input(text="❓ Do you want to play again. \t Type 'y' ot 'n' \n You answer : ",
                             possibilities=['y', 'n'])
    return answer == 'y'



is_game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = 0
# computer_cards = [11, 10]
user_cards = 0
# user_cards = [11, 9]
# print(computer_cards , user_cards)                  # Debugging

computer_score = 0
user_score = 0
# print_stat(comp_cards=computer_cards, us_cards=user_cards, comp_score=computer_score, us_score=user_score, the_user_name=name)

def game():
    global computer_score, user_score, computer_cards, user_cards, logo
    computer_cards = [choice(cards), choice(cards)]
    user_cards = [choice(cards), choice(cards)]
    
    print(logo)
    print("🎇🎇🎆 WELCOME TO MY BLACKJACK GAME 🎆🎇🎇 ")
    name = input("What's your name : ")
    print("Let's Start now \t Choosing of the cards")
    print()

    reset_loop = True
    while reset_loop:
        computer_score = calc_computer_score()
        user_score = calc_user_score()
        print_stat(comp_cards=computer_cards, us_cards=user_cards, comp_score=computer_score, us_score=user_score, the_user_name=name)

        if has_backjack():
            break
        if over_21():
            is_game_over = True
            break
        else:
            if ask_get_another_card():
                reset_loop = True
                draw_another_card()
            else:
                reset_loop = False
                comp_new_card()
                print_stat(comp_cards=computer_cards, us_cards=user_cards, comp_score=computer_score, us_score=user_score, the_user_name=name)

                if comp_over_21():
                    print("Computer score over 21. \t YOU WIN !!! 🏆")
                elif user_score > computer_score:
                    print("You have the highest score. \t YOU WIN !!! 🏆")
                elif user_score < computer_score:
                    print("Computer has the highest score. \t YOU LOOSE !!! 😛")
                elif user_score == computer_score:
                    print("It's a draw 😐")
                            
    
game()

while restart():
    game()
                    
                    
    


    




