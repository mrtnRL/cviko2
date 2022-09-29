from movieModel import MovieModel

pocet = int(input("Zadaj počet filmov: "))
pole_objektov = [pocet]

poradie = 0
for i in range(pocet):
    nazov = ""
    rok_vyroby = ""
    zaner = ""

    pole_objektov[i] = MovieModel(nazov, rok_vyroby, zaner)
