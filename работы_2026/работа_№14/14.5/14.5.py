def max_loot_value():
    n = int(input("введите количество предметов: "))
    values = list(map(int, input("введите ценности предметов: ").split()))

    sorted_values = sorted(values, reverse=True)
    max_value = sum(sorted_values[:n])

    return max_value


print(f"максимальная ценность: {max_loot_value()}")