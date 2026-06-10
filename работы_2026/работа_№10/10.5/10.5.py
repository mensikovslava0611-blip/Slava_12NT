balance = 1000
while True:
    print("\n1 - узнать баланс")
    print("2 - снять 100 руб")
    print("3 - положить 100 руб")
    print("4 - выход")

    choice = input("выберите операцию: ")

    if choice == "1":
        print(f"текущий баланс: {balance} руб")
    elif choice == "2":
        if balance >= 100:
            balance -= 100
            print("снято 100 руб")
        else:
            print("недостаточно средств")
    elif choice == "3":
        balance += 100
        print("положено 100 руб")
    elif choice == "4":
        print("до свидания")
        break
    else:
        print("неверная команда")