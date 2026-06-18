class DungeonMaster:
    def __init__(self, name, vitality_lust):
        self.__name = name
        self.__vitality_lust = vitality_lust

    def get_vitality_lust(self):
        return self.__vitality_lust

    def set_vitality_lust(self, value):
        if 0 < value <= 100:
            self.__vitality_lust = value
        else:
            print('уровень жажды жизненной силы должен быть от 0 до 100!')


value = int(input('Введите уровень крови: '))
billy = DungeonMaster('Билли', 100)
billy.set_vitality_lust(value)
print(f'текущий уровень крови: {billy.get_vitality_lust()}')