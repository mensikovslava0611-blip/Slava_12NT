import random

#случайный вложенный список
nested_list = [[random.randint(1, 50) for _ in range(5)] for _ in range(5)]

row_sums = []  # список сумм по строкам
total_sum = 0  # общая сумма

for row in nested_list:
    row_sum = sum(row)
    row_sums.append(row_sum)
    total_sum += row_sum

max_row_index = row_sums.index(max(row_sums))

print(f"исходный список:\n{nested_list}")
print(f"суммы по строкам: {row_sums}")
print(f"общая сумма: {total_sum}")
print(f"строка с максимальной суммой: {max_row_index}")