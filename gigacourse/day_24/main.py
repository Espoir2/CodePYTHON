with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\my_text.txt") as file:
    contents = file.read()
    print(contents)

# with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\my_text.txt", mode="w") as file:
#     file.write("New text")

with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\my_text.txt", mode="a") as file:
    file.write("\nNew text")

with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\my_text.txt") as file:
    contents = file.read()
    print(contents)
