for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum_powers = a**5 + b**5 + c**5 + d**5
                e = round(sum_powers ** (1/5))
                if e**5 == sum_powers and e <= 150:
                    print(f"Решение найдено: {a} {b} {c} {d} {e}")
                    print(f"Сумма: {a+b+c+d+e}")
                    break