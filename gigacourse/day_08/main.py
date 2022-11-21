from math import *

a, b, c = 1.2, 1.5, 1.8

a2, b2, c2 = round(a), round(b), round(c)
print(a2, b2, c2)

a3, b3, c3 = ceil(a), ceil(b), ceil(c)
print(a3, b3, c3)


# Prime number checker


def fn_checker(nbr):
    result_list = []
    # square_nbr = ceil(sqrt(nbr))
    for i in range(2, nbr):
        result = nbr % i
        result_list.append(result)
    print(result_list)
    if 0 in result_list:
        print(f"{nbr} is not a first number")
    else:
        print(f"{nbr} is a first number")


fn_checker(int(input("Insert your number : ").strip("/*-+ ")))

# 📃Answer :
# We can also use a variable called "is_prime" equals to True at the start
# And to the appropriate condition (if nbr % == 0) in for loop, we can put it at False
# Then, the number will be a first number if is_prime = True

