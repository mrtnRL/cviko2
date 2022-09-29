from film import Film

pocet = int(input("Zadaj počet filmov: "))
pole_objektov = [pocet]

poradie = 0
for i in range(pocet):
    nazov = ""
    rok_vyroby = ""
    zaner = ""

    pole_objektov[i] = Film(nazov, rok_vyroby, zaner)
