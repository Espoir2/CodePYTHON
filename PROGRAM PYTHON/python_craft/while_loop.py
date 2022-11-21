c1 = 0
while c1 < 10:
    print(f"Itération {c1}")
    c1 += 1
    break

print("-"*100)
c2 = 1
while c2 < 10:
    if c2 % 2 == 0:
        continue
        print(f"Itération {c2}")
        c2 += 1
    # if c % 2 == 0:
    #     continue

print("-"*100)

c3 = 0

while c3 < 10:
    print(f"Itération {c3}")
    c3 += 1
    continue

print("-"*100)
