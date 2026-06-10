total = 0
while True:
    price = int(input("введите цену товара: "))
    if price == 0:
        break
    if price < 0:
        print("ошибка цены")
        continue
    total += price

if total > 1000:
    total *= 0.9  #применяем скидку 10%
print(f"итоговая сумма: {total}")