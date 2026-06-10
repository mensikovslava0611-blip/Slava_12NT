price = int(input("Введите сумму: "))
coins = [25, 10, 5, 1]  # Сортируем номиналы по убыванию
count = 0

for coin in coins:
    while price >= coin:
        price -= coin
        count += 1

print(f"Минимальное количество монет: {count}")