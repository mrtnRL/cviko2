class MovieModel:

    def __init__(self, title, description, year, genre, rating) -> None:

        self.title = title
        self.description = description
        self.year = year
        self.genre = genre
        self.rating = rating

        pass

    def genre_to_tring(self):

        return '/'.join(self.genre)

        pass


    def to_string(self) -> None:

        print(f'Title: {self.title:10} | Description: {self.description:20} | Year: {self.year} | Genre: {self.genre} |'
              f'Rating: {self.genre}')

        pass
