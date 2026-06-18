class DungeonMaster:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'я {self.name}, и я хочу кушать!')


d = DungeonMaster('Билли')
d.introduce()