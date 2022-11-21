def separate(symbol="-", nbr=10):
    print(symbol*nbr)

# 💥 Test :
# print("⬜ Function : separate() ⬜")
# separate()

def digit_input(text="Type a number : ",
                error_text="Error! Please check your entry! \n Retry : "):
    digit_str = input(text)
    if not digit_str.isdigit():
        while not digit_str.isdigit():
            digit_str = input(error_text)
    return digit_str


# 💥 Test :
# print("⬜ Function : digit_input() ⬜")
# print(int(digit_input()))
# separate(symbol="=", nbr=30)


def exact_str_input(possibilities, text="Type your answer : ",
                    error_text="Error! Please check your answer!\n Retry : "):
    answer = input(text).lower()
    if answer not in possibilities:
        while answer not in possibilities:
            answer = input(error_text).lower()
    return answer

# 💥 Test :
# print("⬜ Function : exact_str_input() ⬜")
# print(exact_str_input(possibilities=["yes", "no"]))
# separate(symbol="=", nbr=30)


def strip_symbols_input(text="Type your answer : ", symbols=" /*-+.^¨$£¤*µ%!§:#{[|\_@)]=}"):
    return input(text).strip(symbols)

# 💥 Test :
# print("⬜ Function : strip_symbols_input() ⬜")
# print(strip_symbols_input())
# separate(symbol="=", nbr=30)




def print_list(the_list):
    for i in the_list:
        print(i)

# 💥 Test :
# print("⬜ Function : print_list() ⬜")
# print_list(["a", "b", "c"])
# separate(symbol="=", nbr=30)



def print_list_inline(the_list):
    for i in the_list:
        print(i, end=" ")
    print()

# 💥 Test :
# print("⬜ Function : print_list_inline() ⬜")
# print_list(["a", "b", "c"])
# separate(symbol="=", nbr=30)

def print_dictionary(dict):
    for key, value in dict.items():
        print(f"{key} : {value}")

# 💥 Test :
# print("⬜ Function : print_dictionary() ⬜")
# print_dictionary(dict={'a': '1', 'b': '2'})
# separate(symbol="=", nbr=30)


