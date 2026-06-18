class DungeonMaster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def show_info(self):
        print(f'Имя персонажа: {self.name}')
        print(f'Здоровье: {self.hp}')
        print(f'урон: {self.damage}')

gargoyle = DungeonMaster("гаргулья", 120, 18)
gargoyle.show_info()