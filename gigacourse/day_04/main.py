from time import sleep

# New craft with list
my_list2 = ["z", "a", "b","e",  "c"]
my_list3 = [9, 1, 4,  2, 3]

all_list_combine = [my_list2, my_list3]
all_list_sum = [my_list2 + my_list3]

print(all_list_combine)
print(all_list_sum)

# Bulding a map video 7
print("Welcome to my program. We will place the object in a case of this map")
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
print(f"{row1}\n{row2}\n{row3}")


check = True
while check:
    coords = input("Please neter two integers. (Each integers is 1, 2 or 3) :\n")
    if len(coords) != 2 or coords[1] not in ["1", "2", "3"]:
        print("Please check nyour entry (ONLY TWO INTEGERS BETWEEN 1, 2 and 3)")
    elif coords[1] == "1":
        the_row = row1
        check = False
    elif coords[1] == "2":
        the_row = row2
        check = False
    else:
        the_row = row3
        check = False
the_cols = int(coords[0]) -1

the_row[the_cols] = "🔹"

print("\nGreat. Working . . .\n")
sleep(1)

print(f"{row1}\n{row2}\n{row3}")


# ANSWERS
# We can introduce all the row in another list map : map = [row1, row2, row3]
# Then, use the following code to replace the elements of the map : map[x-1][y-1] = "🔹"