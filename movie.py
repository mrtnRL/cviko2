class Movie:

    def __init__(self, name, description, year, genre, rating) -> None:

        self.nazov = name
        self.description = description
        self.rok_vyroby = year
        self.zaner = genre
        self.rating = rating

        pass

    def print_info(self) -> None:

        print(f': Názov filmu: {self.nazov}, rok výroby: {self.rok_vyroby}, žáner: {self.zaner}')


