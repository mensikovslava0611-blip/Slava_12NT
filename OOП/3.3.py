class Inventory:
    def __init__(self, gold):

        self.__gold = gold

    def get_gold(self):

        return f"В кошеле: {self.__gold} проклятых монет"

    def change_gold(self, amount):

        new_balance = self.__gold + amount

        if new_balance < 0:
            print("Недостаточно золота для сделки!")

        else:
            self.__gold = new_balance


if __name__ == "__main__":
    inv = Inventory(100)

    print(inv.get_gold())

    inv.change_gold(50)
    print(inv.get_gold())

    inv.change_gold(-30)
    print(inv.get_gold())

    inv.change_gold(-200)

    print(inv.get_gold())