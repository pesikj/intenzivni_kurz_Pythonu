baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
vstup = input("Zadej číslo balíku: ")
if vstup in baliky:
    if baliky[vstup] == True:
        print("Balík byl předán kurýrovi")
    else:
        print("Balík nebyl předán")
else:
    print("Neznámý balík")
