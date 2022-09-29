class MovieModel:

    def __init__(self, name, description, year, genre, rating) -> None:

        self.name = name
        self.description = description
        self.year = year
        self.genre = genre
        self.rating = rating

        pass

    def toString(self) -> None:

        print(f'Title: {self.name:10}, Description: {self.description:20}, Year: {self.year}, Genre: {self.genre}, '
              f'Rating: {self.genre}')
