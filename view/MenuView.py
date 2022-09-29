from ast import Num

from models.MovieModel import MovieModel


class MenuView:

    def __init__(self) -> None:

        pass

    def menu(self):

        print(f'Welcome to Movie Library')
        print(f'Add Movie')
        print(f'Remove Movie (2)')
        print(f'Show Library (3)')
        print(f'Quit (Q)')

        user_input = input("Select an option from the menu")

        return user_input

    def add_movie(self):

        title:str = input("Enter movie title: ")
        desc:str = input("Enter movie description: ")
        year:Num = Num(input("Enter movie year: "))
        genre:str = input("Enter movie genre: ")
        rating:str = input("Enter movie rating: ")

        return MovieModel(title, desc, year, genre, rating)


    def quit_option(self):

        print("Bye!")
        exit(0)