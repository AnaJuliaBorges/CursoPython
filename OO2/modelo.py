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
        return f'{self.name} - {self.year} - {self.likes} likes'


class Film(Audiovisual):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.year} - {self.duration} min - {self.likes} likes'


class Serie(Audiovisual):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} season(s) - {self.likes} likes'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self.__programs = programs

    @property
    def listing(self):
        return self.__programs

    @property
    def length(self):
        return len(self.__programs)


zfp = Serie('Zoey e sua fantástica playlist', 2020, 1)
zfp.give_likes()
zfp.give_likes()

annie = Film('Annie', 1999, 92)
annie.give_likes()
annie.give_likes()
annie.give_likes()

hsm_series = Serie('High School Musical: A série', 2019, 1)
hsm_series.give_likes()
hsm_series.give_likes()
hsm_series.give_likes()
hsm_series.give_likes()

rent = Film('rent: os boêmios', 2005, 135)
rent.give_likes()

musicals = Playlist('Musicals', [annie, hsm_series, rent, zfp])

print(f'{musicals.name} has {musicals.length} programs')

for program in musicals.listing:
    print(program)
