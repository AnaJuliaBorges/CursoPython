class Audiovisual:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def title(self, title):
        self.__name = title

    @property
    def likes(self):
        return self.__likes

    def give_likes(self):
        self.__likes += 1


class Film(Audiovisual):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Serie(Audiovisual):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season


vingadores = Film('vingadores: guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.give_likes()
vingadores.give_likes()

atlanta.give_likes()

print(f'Nome: {vingadores.name} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.name} - Likes: {atlanta.likes}')
