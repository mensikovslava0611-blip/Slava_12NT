n = int(input("Введите число n: "))
current = 1  # начальная точка отсчёта

while current <= n:
    # проверяем не попадает ли число в запрещённые диапазоны
    if not (5 <= current <= 9 or 17 <= current <= 37 or 78 <= current <= 87):
        print(current)
    current += 1  # Увеличиваем счётчик
