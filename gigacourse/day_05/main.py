# High score getters
scores = input("Enter the scores (Separates each with space\n").strip("/*-+").split()
highest_score = 0

for score in scores:
    score = int(score)
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")
print("-"*100)

# range function range(start_number, end_number+1, step)

# Coding FizzBuzz game

print("WELCOME TO MY FizzBuzz Game")

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

