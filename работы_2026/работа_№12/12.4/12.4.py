marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

count_fives = 0
count_twos = 0

for mark in marks:
    if mark == 5:
        count_fives += 1
    elif mark == 2:
        count_twos += 1

print(f"Количество пятерок: {count_fives}")
print(f"Количество двоек: {count_twos}")