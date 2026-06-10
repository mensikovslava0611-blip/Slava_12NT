number = input("Введите число: ")
digits = [int(d) for d in number]

#подсчет цифр
count_3 = digits.count(3)
last_digit = digits[-1]
count_last = digits.count(last_digit)
count_even = sum(1 for d in digits if d % 2 == 0)
sum_gt5 = sum(d for d in digits if d > 5)
prod_gt7 = 1
count_0_5 = 0

#подсчет произведения и 0/5
for d in digits:
    if d > 7:
        prod_gt7 *= d
    if d == 0 or d == 5:
        count_0_5 += 1

#корректировка произведения
if sum(1 for d in digits if d > 7) == 0:
    prod_gt7 = 1
elif sum(1 for d in digits if d > 7) == 1:
    prod_gt7 = [d for d in digits if d > 7][0]

print(count_3)
print(count_last)
print(count_even)
print(sum_gt5)
print(prod_gt7)
print(count_0_5)