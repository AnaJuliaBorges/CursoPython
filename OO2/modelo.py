class Film:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
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

    @likes.setter
    def give_likes(self):
        self.__likes += 1

class Serie:
    def __init__(self, name, year, season):
        self.__name = name.title()
        self.year = year
        self.season = season
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def give_likes(self):
        self.__likes += 1


vingadores = Film('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.name} - Ano: {vingadores.year} - Duração: {vingadores.duration} minutos')

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.name} - Ano: {atlanta.year} - Temporada: {atlanta.season}')



