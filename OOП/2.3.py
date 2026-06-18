class DungeonMaster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def mutate(self):
        self.power += 5
        print(f'{self.name} подкачался! Сила увеличена! : {self.power} ')

    def rest(self):
        self.hp += 10
        print(f'{self.name} съел протеиновый батончик! Здоровье восстановлено! : {self.hp}')

billy = DungeonMaster('Билли', 100, 10)
billy.mutate()
billy.rest()