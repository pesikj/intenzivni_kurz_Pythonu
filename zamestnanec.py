class Zamestnanec:
    def vybrat_dovolenou(self, pocet_dni):
        if pocet_dni <= self.__dny_dovolene:
            self.__dny_dovolene = self.__dny_dovolene - pocet_dni
            return "Užij si to."
        else:
            return "To už je moc."
    def __str__(self):
        text = f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."
        if self.zkusebni_doba:
            text = text + " Je ve zkušební době."
        return text
    def vypis_attributy(self):
        for polozka in dir(self):
            if not polozka.startswith("__"):
                print(f"{polozka}: {getattr(self, polozka)}")
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.__dny_dovolene = 25
        self.zkusebni_doba = zkusebni_doba
class Manazer(Zamestnanec):
    def __str__(self):
        text = super().__str__()
        text = text + f" Má {self.pocet_podrizenych} podřízených."
        return text
    def __init__(self, jmeno, pozice, zkusebni_doba, pocet_podrizenych):
        super().__init__(jmeno, pozice, zkusebni_doba)
        self.pocet_podrizenych = pocet_podrizenych
class Brigardnik(Zamestnanec):
    def __str__(self):
        text = super().__str__()
        text = text + f" Zaměstnanec má úvazek {self.velikost_uvazku}."
        return text
    def __init__(self, jmeno, pozice, zkusebni_doba, velikost_uvazku):
        self.velikost_uvazku = velikost_uvazku
        super().__init__(jmeno, pozice, zkusebni_doba)
frantisek = Zamestnanec(pozice="konstruktér", jmeno="František Novák", zkusebni_doba=True)
#klara = Zamestnanec("Klára Nová", "konstruktérka", "123", "KN", 30, False)
# marian = Manazer("Marian Přísný", "vedoucí KO", False, 2)
# marian.vypis_attributy()
brigadnik = Brigardnik("Jirka", "asistent", False, 0.5)
print(brigadnik)