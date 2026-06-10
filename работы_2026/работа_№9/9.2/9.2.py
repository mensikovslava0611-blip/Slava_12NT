count = 0
found_alexandra = False

while True:
    name = input().strip()

    if name == "Александра":
        found_alexandra = True
    elif name == "Левон":
        break
    elif found_alexandra:
        count += 1

print(count)