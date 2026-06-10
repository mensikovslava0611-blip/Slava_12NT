max_number = 0
while True:
    number = int(input("введите число (0 для выхода): "))
    if number == 0:
        break
    if number > max_number:
        max_number = number
print(f"максимальное число: {max_number}")