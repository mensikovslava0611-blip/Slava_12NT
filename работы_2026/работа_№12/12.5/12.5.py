data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
reversed_list = data[::-1]
odd_index = data[1::2]

print(f"Первые три числа: {first_three}")
print(f"Последние три числа: {last_three}")
print(f"Обратный порядок: {reversed_list}")
print(f"Элементы с нечетными индексами: {odd_index}")