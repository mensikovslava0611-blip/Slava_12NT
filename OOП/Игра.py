import random


class Monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def take_damage(self, dmg):
        self.__hp -= dmg
        if self.__hp < 0:
            self.__hp = 0

    def attack_hunter(self, hunter):
        hunter.take_damage(self.__dmg)
        print(f'{self.__name} атакует охотника! Охотник теряет {self.__dmg} HP. У охотника осталось: {hunter.get_hp()}')

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print(f'Монстр {self.__name}: {self.__hp} HP')


class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 175
        self.__weapons = []

    def take_damage(self, dmg):
        self.__hp -= dmg
        if self.__hp < 0:
            self.__hp = 0

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def add_weapon(self, weapon):
        self.__weapons.append(weapon)
        print(f"{self.__name} подобрал оружие: {weapon.name}")

    def show_inventory(self):
        if not self.__weapons:
            print(f"У {self.__name} нет оружия.")
        else:
            print(f"Инвентарь {self.__name}:")
            for i, w in enumerate(self.__weapons, 1):
                print(f"  {i}. {w.name}")

    def attack(self, weapon_index, monster):

        if 0 <= weapon_index < len(self.__weapons):
            weapon = self.__weapons[weapon_index]
            print(f"{self.__name} использует {weapon.name} против {monster.get_name()}!")
            weapon.use(monster)
        else:
            print("Неверный номер оружия!")

    def is_alive(self):
        return self.__hp > 0


class Zombie(Monster):
    def __init__(self, name):
        super().__init__(name, hp=120, dmg=10)

    def take_damage(self, dmg):
        super().take_damage(dmg)
        print(f'{self.get_name()} теряет конечность! Получено: {dmg}. HP: {self.get_hp()}')


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, hp=80, dmg=15)

    def take_damage(self, dmg):
        absorbed = 5
        actual_damage = max(0, dmg - absorbed)
        super().take_damage(actual_damage)
        print(f'{self.get_name()} поглощает {absorbed} урона! Получено: {actual_damage}. HP: {self.get_hp()}')


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, hp=60, dmg=20)

    def take_damage(self, dmg):
        evade_chance = 0.3
        if random.random() < evade_chance:
            print(f'{self.get_name()} уклонился от удара! Получено: 0. HP: {self.get_hp()}')
        else:
            super().take_damage(dmg)
            print(f'{self.get_name()} не смог уклониться. Получено: {dmg}. HP: {self.get_hp()}')


class Werewolf(Monster):
    def __init__(self, name):
        super().__init__(name, hp=100, dmg=25)
        self.transformed = False

    def take_damage(self, dmg):
        super().take_damage(dmg)
        if self.get_hp() < 50 and not self.transformed:
            self.transformed = True
            print(f'{self.get_name()} трансформируется из‑за низкого HP! HP: {self.get_hp()}')
        else:
            print(f'{self.get_name()} получил {dmg} урона. HP: {self.get_hp()}')


class Weapon:
    def __init__(self, name):
        self.name = name


class SilverSword(Weapon):
    def __init__(self):
        super().__init__("Серебряный меч")
        self.dmg = 30

    def use(self, monster):
        print(f"Серебряный меч наносит удар! Урон: {self.dmg}")
        monster.take_damage(self.dmg)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__("Святая вода")
        self.dmg = 20

    def use(self, monster):
        print(f"Святая вода обжигает монстра! Урон: {self.dmg}")
        monster.take_damage(self.dmg)


class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__("Арбалет с болтом")
        self.dmg = 25

    def use(self, monster):
        print(f"Болт арбалета попадает в цель! Урон: {self.dmg}")
        monster.take_damage(self.dmg)


def run_game():

    hunter = Hunter("Ван Хельсинг")
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(CrossbowBolt())


    hunter.show_inventory()


    monsters = [
        Zombie("Зондре"),
        Vampire("Алукард"),
        Ghost("Пожиратель душь"),
        Werewolf("Пудель оборотень")
    ]

    print("\n=== НАЧАЛО БИТВЫ ===\n")

    for monster in monsters:
        print(f"\nСражение с {monster.get_name()} (HP: {monster.get_hp()})")
        monster.show_status()


        while monster.is_alive() and hunter.is_alive():

            weapon_index = 0
            hunter.attack(weapon_index, monster)

            if monster.is_alive():
                monster.attack_hunter(hunter)


            print(f"Статус охотника: HP = {hunter.get_hp()}")

        if not hunter.is_alive():
            print("\n ПОРАЖЕНИЕ: Ван Хельсинг пал в бою...")
            return

        print(f"\nПобеда над {monster.get_name()}! Переход к следующему отродью.")

    print("\n ПОБЕДА: Все монстры НИЗВЕДЕНЫ ДО АТОМОВ, мир может спать спокойно! ")


if __name__ == "__main__":
    run_game()
