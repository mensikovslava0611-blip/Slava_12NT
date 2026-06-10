#число от пользователя
n = int(input("Введите число n: "))

#список нечетных чисел
odd_numbers = [i for i in range(1, n+1) if i % 2 != 0]

print(f"Список нечетных чисел: {odd_numbers}")