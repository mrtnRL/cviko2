class Film:

    def __init__(self, nazov, rok_vyroby, zaner) -> None:

        self.nazov = nazov
        self.rok_vyroby = rok_vyroby
        self.zaner = zaner

    def print_info(self) -> None:

        print(f': Názov filmu: {self.nazov}, rok výroby: {self.rok_vyroby}, žáner: {self.zaner}')


