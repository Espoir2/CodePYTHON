from pprint import pprint
from random import *

possibilities = ["0", "1", "2"]

print("""
      
        WELCOME TO MY *ROCK* *PAPER* *SCISSORS* GAME
        
      """)

check = True
while check:
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")
    if len(user_choice) != 1 or user_choice not in possibilities:
        print("Please check your entry (ONLY  0, 1 or 2 )")
    elif user_choice == "0":
        print("You  choose : ")
        print(""" 
        Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
        """)
        check = False
    elif user_choice == "1":
        print("You choose : ")
        print("""
        Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
        """)
        check = False
    else:
        print("You choose : ")
        print("""
        Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
        """)
        check = False

computer_choice = choice(possibilities)
if computer_choice == "0":
    print("Computer choose : ")
    print(""" 
            Rock
              _______
          ---'   ____)
                (_____)
                (_____)
                (____)
          ---.__(___)
            """)
elif computer_choice == "1":
    print("Computer choose : ")
    print("""
            Paper
              _______
          ---'   ____)____
                    ______)
                    _______)
                   _______)
          ---.__________)
            """)
else:
    print("Computer choose : ")
    print("""
            Scissors
              _______
          ---'   ____)____
                    ______)
                 __________)
                (____)
          ---.__(___)
            """)

if computer_choice == user_choice:
    print("It's a draw")
elif (computer_choice == "0" and user_choice == "2") or (computer_choice == "1" and user_choice == "0") or (
        computer_choice == "2" and user_choice == "1"):
    print("You loose 😛")
else:
    print("You win🏆")