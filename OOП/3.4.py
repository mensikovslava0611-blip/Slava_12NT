class Werewolf:
    def __init__(self, name):

        self.__name = name
        self.__form = "Человек"
        self.__power = 15

    def get_stats(self):

        print(f"{self.__name} сейчас в форме: {self.__form}. Сила: {self.__power}")

    def transform(self):

        if self.__form == "Человек":
            self.__form = "Волк"
            self.__power = 45
            print(f"{self.__name} обрастает шерстью!")
        elif self.__form == "Волк":
            self.__form = "Человек"
            self.__power = 15
            print(f"{self.__name} снова становится человеком.")



if __name__ == "__main__":
    wolf = Werewolf("Люкан")

    wolf.get_stats()
    wolf.transform()
    wolf.get_stats()
    wolf.transform()
    wolf.get_stats()