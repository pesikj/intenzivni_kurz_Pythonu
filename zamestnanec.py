class Zamestnanec:
    def vybrat_dovolenou(self, pocet_dni):
        if pocet_dni <= self.dny_dovolene:
            self.dny_dovolene = self.dny_dovolene - pocet_dni
            return "Užij si to."
        else:
            return "To už je moc."
    def __str__(self):
        text = f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."
        if self.zkusebni_doba:
            text = text + " Je ve zkušební době."
        return text
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.dny_dovolene = 25
        self.zkusebni_doba = zkusebni_doba
class Manazer(Zamestnanec):
    def __str__(self):
        text = super().__str__()
        text = text + f" Má {self.pocet_podrizenych} podřízených."
        return text
    def __init__(self, jmeno, pozice, zkusebni_doba, pocet_podrizenych):
        super().__init__(jmeno, pozice, zkusebni_doba)
        self.pocet_podrizenych = pocet_podrizenych
frantisek = Zamestnanec(pozice="konstruktér", jmeno="František Novák", zkusebni_doba=True)
#klara = Zamestnanec("Klára Nová", "konstruktérka", "123", "KN", 30, False)
marian = Manazer("Marian Přísný", "vedoucí KO", False, 2)
print(marian.vybrat_dovolenou(20))
print(marian.vybrat_dovolenou(10))
print(marian)

