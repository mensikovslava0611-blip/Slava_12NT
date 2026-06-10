number = input("Введите число: ")
digits = list(number)  # Преобразуем в список цифр

# Инициализируем счётчики
count_3 = 0
last_digit_count = 0
even_count = 0
sum_over_5 = 0
product_over_7 = 1
zero_five_count = 0
found_over_7 = False

for digit in digits:
    digit = int(digit)

    # 1. Считаем цифру 3
    if digit == 3:
        count_3 += 1

    # 2. Считаем последнюю цифру
    if digit == int(digits[-1]):
        last_digit_count += 1

    # 3. Считаем чётные цифры
    if digit % 2 == 0:
        even_count += 1

    # 4. Суммируем цифры > 5
    if digit > 5:
        sum_over_5 += digit

    # 5. Считаем произведение цифр > 7
    if digit > 7:
        product_over_7 *= digit
        found_over_7 = True

    # 6. Считаем 0 и 5
    if digit == 0 or digit == 5:
        zero_five_count += 1

# Корректируем произведение
if not found_over_7:
    product_over_7 = 1
elif sum(1 for d in digits if int(d) > 7) == 1:
    product_over_7 = next(int(d) for d in digits if int(d) > 7)

# Выводим результаты
print(count_3)
print(last_digit_count)
print(even_count)
print(sum_over_5)
print(product_over_7)
print(zero_five_count)