from models.movieModel import MovieModel


class MovieLibraryService:

    def __init__(self) -> None:

        self.movies:list = list()
        pass

    def add_movie(self, movie:MovieModel):

        self.movies.append(movie)
        pass

    def remove_movie(self, movie_index):

        self.movies.pop(movie_index)
        pass

    def to_string(self):

        print("************************ MOVIE LIBRARY ************************")

        for movie in self.movies:
            print(movie.to_string)
            print("")

        print("")
