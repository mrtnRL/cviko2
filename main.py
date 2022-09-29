from movie import Movie

pocet = int(input("Zadaj počet filmov: "))
pole_objektov = [pocet]

poradie = 0
for i in range(pocet):
    nazov = ""
    rok_vyroby = ""
    zaner = ""

    pole_objektov[i] = Movie(nazov, rok_vyroby, zaner)
