from math import *
from random import *

# 🔷 List comprehension
print("="*10, "List comprehension", "="*10)
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# for n in numbers:
#      n+=1
#    new_numbers.append(n)
print(numbers)
print(new_numbers)

name = "Espoir"
letters_list = [letter for letter in name]
print(letters_list)

nbr_range = [n * 2 for n in range(1, 5)]
print(nbr_range)
print()


# 🔷Conditional list comprehension
print("="*10, "Conditional list comprehension", "="*10)
nbr_list = [1, 5, 58, 8, 9, 54, 65, 21]
new_nbr_list = [nbr for nbr in nbr_list if nbr > (sum(nbr_list)/len(nbr_list))]
print(new_nbr_list)
print()

# ⚪Coding exercise §§ Squared fibonacci number
print("*"*5, "Squared fibonacci number", "*"*5)
fibonacci = []
b = 1
a = 0
for c in range(10):
    d = a + b
    a = b
    b = d
    fibonacci.append(b)
print(fibonacci)
fibonacci_square = [nbr**2 for nbr in fibonacci]
print(fibonacci_square)
print()

# ⚪Coding exercise   §§ Print the even number between 1 and 20
print("*"*5, "Even Number", "*"*5)

nbr_list = [i for i in range(1, 20+1) if i % 2 == 0]
print(nbr_list)
print()

#  ⚪Coding exercise   §§ Print the number that are simultaneously in two files
print("*"*5, "Matching number in two files", "*"*5)

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()
result = [int(num) for num in file1_data if num in file2_data]
# for i in file1_data:
#     result.extend(i.strip() for j in file2_data if i == j)

print(result)
print("="*55)
print()

# 🔷Dictionary comprehension
print("="*10, "Conditional list comprehension", "="*10)

names = ["Espoir", "Nahim", "Vladimir", "Méleck", "Hishaam", "René"]
students_scores = {student: randint(1, 100) for student in names}
print(students_scores)
average_score = 0
for student in students_scores:
    average_score += students_scores[student]
average_score /= len(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > average_score}
print(f"Average is : {average_score}")
print(passed_students)
print()

# ⚪ Coding exercise   §§ Get each sentence of a sentence with the length of each of thes words
print("*"*5, "Word in a sentence", "*"*5)
sentence = "Espoir and his team have a great determination to success"
sentence_list = sentence.split()
print(sentence_list)
my_dict = {word: len(word) for word in sentence_list}
print(my_dict)
print()

# ⚪ Coding exercise   §§ Convert temperature in Celsius in Fahrenheit
print("*"*5, "Celsius to fahrenheit", "*"*5)

dict_c = {"Monday": randint(1, 40),
          "Tuesday": randint(1, 40),
          "Wednesday": randint(1, 40),
          "Thursday": randint(1, 40),
          "Friday": randint(1, 40),
          "Saturday": randint(1, 40),
          "Sunday": randint(1, 40)}

dict_f = {day: (temp * 9/5) + 32 for (day, temp) in dict_c.items()}
print(dict_f)
print()


# 🔷 Iterate data with Pandas
print("="*10, "Pandas", "="*10)
from pandas import *

travel_dict = {
    "states": ["USA", "Canada", "Italie", "Russie"],
    "Price": [500, 450, 375, 500]
}
travel_pandas = DataFrame(travel_dict)

print("*"*5, "Print Pandas", "*"*5)
print(travel_pandas)
print("*"*5)
print()

print("*"*5, "Print key", "*"*5)
for (key, value) in travel_pandas.items():
    print(key)
print("*"*5)
print()

print("*"*5, "Print value", "*"*5)
for (key, value) in travel_pandas.items():
    print(value)
print("*"*5)
print()

print("*"*5, "Print key : value", "*"*5)
for (key, value) in travel_pandas.items():
    print(key, ":", value)
print("*"*5)
print()

print("*"*5, "Print index", "*"*5)
for (index, row) in travel_pandas.iterrows():
    print(index)
print("*"*5)
print()


print("*"*5, "Print row", "*"*5)
for (index, row) in travel_pandas.iterrows():
    print(row)
    print("💥")
print("*"*5)
print()

print("*"*5, "Print specific element in row", "*"*5)
for (index, row) in travel_pandas.iterrows():
    print(row.states)
print("*"*5)
print()

