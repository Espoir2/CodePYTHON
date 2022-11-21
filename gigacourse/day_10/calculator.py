from eslib import print_list_inline, exact_str_input, digit_input


#########################################
# 🔴 Define function for each operation #
#########################################
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# operations = {
#     "+": add(nbr_01, nbr_02),
#     "-": subtract(nbr_01, nbr_02),
#     "*": multiply(nbr_01, nbr_02),
#     "/": divide(nbr_01, nbr_02),
# }


########################################
# 🔴🔴 Stock function in a dictionary #
########################################
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


###############################################
# 🔴🔴🔴 Define the main function calculator #
###############################################
def calculator():
    
    print("""
_____________________
|  _________________  |
| | Espoir       0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
          """, end=" ")
    
    
    print("""
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
          """)
    nbr_01 = float(digit_input(text="Type your first number : "))
    nbr_02 = float(digit_input(text="Type your second number : "))

    for key in operations:
        print(key)

    operation_symbol = exact_str_input(possibilities=["+", "-", "*", "/"],
                                       text="Chooses an operation symbol : \n")
    calculation_function = operations[operation_symbol]
    result = calculation_function(nbr_01, nbr_02)

    print("💥💥💥💥💥 Result 💥💥💥💥💥")
    print(f"{nbr_01} {operation_symbol} {nbr_02} = {result}")
    print("-" * 20)

    should_continue = True
    while should_continue:  # 🔄 While loop to continue with the last result
        ask = exact_str_input(
            possibilities=["next", "reset", "quit"],
            text=f"""
🔷 Type 'next' to continue with {result} 
🔷 Type 'reset' to restart another calculation
🔷 Type 'quit' to exit \n Your answer : """)

        if ask == "quit":
            should_continue = False
            print("GoodBye🖐")
            break
        elif ask == "next":
            print()
            print("SO CONTINUE")
            nbr_next = float(digit_input(text="What is the next number ? \n"))
            for key in operations:
                print(key)
            operation_symbol = exact_str_input(possibilities=["+", "-", "*", "/"],
                                               text="Pick another operation symbol \n")

            result_next = operations[operation_symbol](result, nbr_next)
            print("💥💥💥💥💥 Result 💥💥💥💥💥")
            print(f"{result} {operation_symbol} {nbr_next} = {result_next}")
            result = result_next
            print("-" * 20)
        elif ask == "reset":
            calculator()  # 🔄 To restart a new calculator


calculator()

# for key, value in operations.items():
# print(f"{key} : {value}")
