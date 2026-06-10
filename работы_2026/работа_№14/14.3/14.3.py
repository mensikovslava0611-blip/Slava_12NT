import random

#случайный вложенный список
nested_list = [[random.randint(-20, 20) for _ in range(5)] for _ in range(5)]

#отфильтрованный список
filtered_list = [[x for x in row if x > 0] for row in nested_list]

print(f"исходный список:\n{nested_list}")
print(f"отфильтрованный список:\n{filtered_list}")