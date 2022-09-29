from constants.MenuActionEnum import MenuActionEnum
from models.MovieModel import MovieModel
from services.MovieLibraryService import MovieLibraryService
from view.MenuView import MenuView

she_hulk = MovieModel("She-Hulk", "Jennifer Walters navigates the complicated life of a single, "
                                  "30-something attorney who also happens to be a green 6-foot-7-inch"
                                  "superpowered Hulk.", 2022, "action", 5 / 10)

movie_library = MovieLibraryService()
movie_library.add_movie(she_hulk)
movie_library.add_movie(she_hulk)
movie_library.to_string()
movie_library.remove_movie(0)
movie_library.to_string()

#print(she_hulk.to_string())

menu_view = MenuView()

while True:

    match menu_view.menu():

        case MenuActionEnum.ADD_MOVIE:
            movie_library.add_movie(menu_view.add_movie())
            pass

        case MenuActionEnum.REMOVE_MOVIE:
            pass

        case MenuActionEnum.SHOW_LIBRARY:
            movie_library.to_string()
            pass

        case MenuActionEnum.QUIT:
            menu_view.quit_option()
            exit(0)
            pass



