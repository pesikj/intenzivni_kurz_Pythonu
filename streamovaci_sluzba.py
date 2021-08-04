class Polozka:
    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}"
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
class Film(Polozka):
    def get_celkova_delka(self):
        return self.delka
    def get_info(self):
        text = super().get_info()
        return text + f" Délka filmu je {self.delka}"
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
class Serial(Polozka):
    def get_celkova_delka(self):
        return self.delka_epizody * self.pocet_epizod
    def get_info(self):
        text = super().get_info()
        return text + f" Seriál má {self.pocet_epizod} epizod a jedna epizoda má délku {self.delka_epizody}."
    def __init__(self, nazev, zanr, delka_epizody, pocet_epizod):
        super().__init__(nazev, zanr)
        self.delka_epizody = delka_epizody
        self.pocet_epizod = pocet_epizod
class Uzivatel:
    def pripocti_zhlednuti(self, polozka):
        self.delka_sledovani = self.delka_sledovani + polozka.get_celkova_delka()
    def pripocti_zhlednuti_seznam(self, polozka):
        self.seznam_zhlednutych_polozek.append(polozka)
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
        self.seznam_zhlednutych_polozek = []
film = Film("Film 1", "historický", 90)
serial = Serial("Seriál 1", "sci-fi", 70, 30)
uzivatel = Uzivatel("Jirka")
uzivatel.pripocti_zhlednuti(film)
uzivatel.pripocti_zhlednuti(serial)
print(uzivatel.delka_sledovani)
