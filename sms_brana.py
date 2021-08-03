import math
def over_cislo(cislo):
    if not cislo.isnumeric():
        return False
    if cislo[0:4] == "+420" and len(cislo) == 13 or len(cislo) == 9:
        return True
    else:
        return False
def cena_zpravy(zprava):
    return math.ceil(len(zprava) / 180) * 3

cislo = input("Zadej telefonní číslo: ")
if over_cislo(cislo):
    zprava = input("Zadej text zprávy: ")
    print(f"Cena zprávy je {cena_zpravy(zprava)}")