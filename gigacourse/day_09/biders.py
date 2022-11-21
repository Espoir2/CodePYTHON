# from replit import clear
print("""
                                 
88          88          88  
88          ""          88  
88                      88  
88,dPPYba,  88  ,adPPYb,88  
88P'    "8a 88 a8"    `Y88  
88       d8 88 8b       88  
88b,   ,a8" 88 "8a,   ,d88  
8Y"Ybbd8"'  88  `"8bbdP"Y8  
                            
      """)

bidders = {}

# 🟠 Get the name and the price of each bidder and stock it in a dictionary
should_continue = True
while should_continue:
    name = input("What is your name ? \n")  # 🔹 Name

    price_str = ""
    while not price_str.isdigit():
        price_str = input("Type your bid : $")  # 🔹 Price
    price = int(price_str)

    bidders[name] = price  # 🔹 Stock it
    # 🟠🟠 Check it there are another bidder
    check = False
    while not check:
        ask_should_continue = input("Are there any another bidders ? Type 'yes' or 'no' :\n ").lower()
        if ask_should_continue in ["yes", "no"]:
            check = True

    if ask_should_continue == "no":
        should_continue = False
        print("Check the result here 👇")

# print(bidders)

# 🟠🟠🟠 Get the result of the bid
the_greatest_price = 0
for bidder in bidders:
    if bidders[bidder] > the_greatest_price:
        the_greatest_price = bidders[bidder]
        the_greatest_bidder = bidder
print(f"The winner is {the_greatest_bidder} with {the_greatest_price}")

# Answer craft
# The best way is to structure the code in two part :
# A  first part to define the function that find the greatest_bidder and a second part
# For a while_loop that get the bit and stock it. Then with a conditional structure
# call the last function in the appropriate case
