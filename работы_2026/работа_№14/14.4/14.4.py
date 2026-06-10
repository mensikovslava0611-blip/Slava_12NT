import random

#случайный вложенный список
nested_list = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
search_value = int(input("Введите значение для поиска: "))

positions = []  #список найденных позиций

#поиск элемента
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        if nested_list[i][j] == search_value:
            positions.append((i, j))

print(f"исходный список:\n{nested_list}")
print(f"значение {search_value} найдено на позициях: {positions}")