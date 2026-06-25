class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

data1 = input().split()
name1 = data1[0]
hp1 = int(data1[1])
dmg1 = int(data1[2])

data2 = input().split()
name2 = data2[0]
hp2 = int(data2[1])
dmg2 = int(data2[2])

m1 = Monster(name1, hp1, dmg1)
m2 = Monster(name2, hp2, dmg2)