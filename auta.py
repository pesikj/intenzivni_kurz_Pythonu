class Auto:
    def get_info(self):
        return f"{self.znacka_a_typ}, reg. zn. {self.reg_znacka}"
    def vrat_auto(self, pocet_dni, stav_tachometru):
        self.pocet_km = stav_tachometru
        self.volne = True
        if pocet_dni < 7:
            return pocet_dni * 400
        else:
            return pocet_dni * 300
    def pujc_auto(self):
        if self.volne == True:
            self.volne = False
            return "Povrzuji půjčení auta."
        else:
            return "Vozidlo není k dispozici."
    def __init__(self, reg_znacka, znacka_a_typ, pocet_km):
        self.reg_znacka = reg_znacka
        self.znacka_a_typ = znacka_a_typ
        self.pocet_km = pocet_km
        self.volne = True
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
print(auto1.pujc_auto())
print(auto1.vrat_auto(10, 50000))
print(auto1.pujc_auto())
# seznam_aut = [
#     Auto("4A2 3020", "Peugeot 403 Cabrio", 47534),
#     Auto("4A2 3021", "Peugeot 403 Cabrio", 47534),
#     Auto("1P3 4747", "Škoda Octavia", 41253)
# ]
# pozadovane_auto = input("Zadej značku auta (možnosti: Škoda, Peugeot): ")
# for auto in seznam_aut:
#     if pozadovane_auto in auto.znacka_a_typ:
#         print(auto.get_info())

pozadovane_auto = input("Zadej značku auta (možnosti: Škoda, Peugeot): ")
if pozadovane_auto == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif pozadovane_auto == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Neznámé auto")

# seznam_aut = [
#     Auto("4A2 3020", "Peugeot 403 Cabrio", 47534),
#     Auto("1P3 4747", "Škoda Octavia", 41253)
# ]
# slovnik_s_auty = {
#     "4A2 3020": Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
# }