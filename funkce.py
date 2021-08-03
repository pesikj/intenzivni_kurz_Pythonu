# Násobení
def mult(a, b):
    return a * b
#print(mult(5, 8))
# Hotel
def totalPrice(persons, breakfast=False):
    if breakfast == True:
        return persons * 925
    else:
        return persons * 850
#persons = int(input("Zadej počet osob"))
#breakfast = input("Snídaně ano/ne: ")
#breakfast = breakfast == "ano"
#print(breakfast)
#print(totalPrice(persons, breakfast))

# retezec = "květen"
# delka = len(retezec)
# print(retezec[:2])

# def monthOfBirth(birthNumber):
#     month = birthNumber[2:4]
#     month = int(month)
#     if month > 50:
#         month = month - 50
#     return month % 50
# print(monthOfBirth("9555125899"))
import random
def roulette(cislo, rada):
    rada1 = [1, 4, 7, 10, 13]
    rada2 = [2, 5, 8, 11, 14]
    rada3 = [3, 6, 9, 12, 15]
    if rada == 1 and cislo in rada1:
        return True
    if rada == 2 and cislo in rada2:
        return True
    if rada == 3 and cislo in rada3:
        return True
    return False
rada = int(input("Zadej číslo řady: "))
cislo = random.randint(0, 15)
print(f"Padlo číslo {cislo}")
print(f"Výhra: {roulette(cislo, rada)}")

