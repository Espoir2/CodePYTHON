# Function with outputs

nbr = int(input("Type an positive number : "))


def even_number(number):
    """I add my first docString"""
    if number % 2 == 0:
        return True
    return False



if even_number(nbr):
    print(f"{nbr} is an even number")
else:
    print(f"{nbr} is not an even number")

