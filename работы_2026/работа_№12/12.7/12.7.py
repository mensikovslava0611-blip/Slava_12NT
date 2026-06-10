#исходный список
numbers = [10, 20, 30, 40, 50]

#число для поиска от пользователя
search_number = int(input("Введите число для поиска: "))

for i in range(len(numbers)):
    if numbers[i] == search_number:
        print(f"Число {search_number} найдено по индексу {i}")
        break
else:
    print("Нет такого числа в списке")