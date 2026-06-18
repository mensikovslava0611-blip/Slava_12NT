class DungeonMaster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


    def bite(self, damage):
        self.hp -= damage
        return self.hp


billy = DungeonMaster('Билли', 100, )
damage = int(input('Введите силу укуса: '))
remaining_hp = billy.bite(damage)
print('Оставшееся здоровье: ', remaining_hp)

