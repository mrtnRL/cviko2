from models.movieModel import MovieModel
from services.MovieLibraryService import MovieLibraryService

she_hulk = MovieModel("She-Hulk", "Jennifer Walters navigates the complicated life of a single, "
                                  "30-something attorney who also happens to be a green 6-foot-7-inch"
                                  "superpowered Hulk.", 2022, "action", 5 / 10)

print(she_hulk.to_string())

movie_library = MovieLibraryService()
movie_library.add_movie(she_hulk)
movie_library.add_movie(she_hulk)
movie_library.to_string()
movie_library.remove_movie(0)
movie_library.to_string()
