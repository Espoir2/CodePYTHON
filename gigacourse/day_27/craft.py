def unlimited_arguments(*args):
    print(f"First element of args : {args[0]}")
    for n in args:
        print(n)

unlimited_arguments("arg1", "arg2", "arg3", 7)

# Create a sum fonction

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(25, 45))

# Kwargs
print("🔷🔷 Calculate function 🔷🔷")
def calculate(n, **kwargs):
    for i in kwargs:
        print(i)
    print()

    for (key, value) in kwargs.items():
        print(f"{key} : {value}")

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=2, multiply=3)