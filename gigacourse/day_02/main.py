print("Hello"[0])
print("Espoir"[3])

print("-"*100)
print("-"*100)



# Making of a addition calculator

nbr_str = input("Please enter a digit number : ").strip(" +*/.-")
if len(nbr_str) == 1 :
    print(f"The result is : {nbr_str}")
else:   
    liste = []
    while len(nbr_str) > 1 :
        liste = []
        for i in nbr_str:
            i_int = int(i)
            print(i_int, type(i_int))
            liste.append(i_int)
        nbr_str = str(sum(liste))
        print(f"The result is : {nbr_str}")
    
# round(8/3, 2) : permit to round the result with two number after the coma ou bien utiliser : "{:.2f}".format(8/3)
