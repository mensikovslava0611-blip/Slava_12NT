import random

#случайный вложенный список
nested_list = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]

#переменные для поиска максимума
max_value = nested_list[0][0]
max_row = 0
max_col = 0


for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        if nested_list[i][j] > max_value:
            max_value = nested_list[i][j]
            max_row = i
            max_col = j

print(f"исходный список:\n{nested_list}")
print(f"максимальный элемент: {max_value}")
print(f"позиция: строка {max_row}, столбец {max_col}")