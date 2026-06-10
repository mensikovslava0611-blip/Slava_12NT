prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
total_sum = sum(prices)
average_price = total_sum / len(prices)

print(f"Самая высокая цена: {max_price}")
print(f"Самая низкая цена: {min_price}")
print(f"Общая стоимость: {total_sum}")
print(f"Средняя цена: {average_price:.2f}")