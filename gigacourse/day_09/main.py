# 🔷🔷🔷 DICTIONARY 🔷🔷🔷
print("-" * 10, "DICTIONARY", "-" * 10)

my_dictionnary = {
    'key_01': 'element_01',
    'key_02': 'element_02',
    'key_03': 'element_03',

}

for key in my_dictionnary:
    print(key)
print("-" * 50)
for key in my_dictionnary:
    print(f"{key} : {my_dictionnary[key]}")

print("=" * 50)

# Converting students scores into grades

students_scores = {
    'espoir': 16.7,
    'nahim': 16.6,
    'amael': 14,
    'esperan': 15,
    'kinede': 11,
    'prico': 13,
    'hisham': 18,
    'terrence': 9,
}

students_grades = {}

for student in students_scores:
    if students_scores[student] >= 18:
        students_grades[student] = "Excellent"
    elif students_scores[student] >= 16:
        students_grades[student] = "Très bien"
    elif students_scores[student] >= 14:
        students_grades[student] = "Bien"
    elif students_scores[student] >= 12:
        students_grades[student] = "Assez bien"
    elif students_scores[student] >= 10:
        students_grades[student] = "Passable"
    else:
        students_grades[student] = "Ajourné"

for key in students_scores:
    print(f"{key} : {students_scores[key]}")

print("-" * 50)

for key in students_grades:
    print(f"{key} : {students_grades[key]}")

print()

# 🔷🔷🔷 NESTING 🔷🔷🔷
print("-" * 10, "NESTING", "-" * 10)

# 🔷 Dictionary in a dictionary, list in a dictionary 🔷

machine_brand = {
    "Computer": {"brands": ['Apple', 'Asus', 'Hp', 'Toshiba'], "total": 4},
    "Phone": {"brands": ['Iphone', 'Techno', 'Infinix', 'Samsung', 'Huawei'], "total": 5}
}

for element in machine_brand:
    print(element)
    print(machine_brand[element])
    print("-" * 10)

# 🔷 Dictionary in a list 🔷

machine_brand_02 = [
    {"machine_type": "Computer",
     "brands": ['Apple', 'Asus', 'Hp', 'Toshiba'],
     "total": 4},

    {"machine_type": "Phone",
     "brands": ['Iphone', 'Techno', 'Infinix', 'Samsung', 'Huawei'],
     "total": 5},
]


# Exercise with dictionary in a list
print("👇" * 10)
def add_new_machine(the_machine_type, diferent_brand, total_brands):
    global machine_brand_02
    the_new_dictionary = {
        "machine_type": the_machine_type,
        "brands": diferent_brand,
        "total": total_brands
    }

    machine_brand_02.append(the_new_dictionary)

add_new_machine(the_machine_type="car", diferent_brand=['Tesla', 'Lamborghini', 'Ford T', 'Ferrari'], total_brands=4)
print(machine_brand_02)
print("-"*10)

for element in machine_brand_02:
    print(element)

print("-"*10)
for i in range(len(machine_brand_02)):
    for element in machine_brand_02[i]:
        print(element, ":", machine_brand_02[i][element])
    print("=== END ELEMENT ===")

print("👆" * 10)

