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

    def __str__(self):
        return f'{program.name} - {program.year} - {program.likes} likes'


class Film(Audiovisual):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{program.name} - {program.year} - {program.duration} min - {program.likes} likes'

class Serie(Audiovisual):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{program.name} - {program.year} - {program.seasons} seasons - {program.likes} likes'

vingadores = Film('vingadores: guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.give_likes()
vingadores.give_likes()

atlanta.give_likes()

list = [atlanta, vingadores]

for program in list:
    print(program)