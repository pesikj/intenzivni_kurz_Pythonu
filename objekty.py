class Zamestnanec:
    def vybrat_dovolenou(self, pocet_dni):
        if pocet_dni <= self.dny_dovolene:
            self.dny_dovolene = self.dny_dovolene - pocet_dni
            return "Užij si to."
        else:
            return "To už je moc."
    def __str__(self):
        return f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."
    def __init__(self, jmeno, pozice, rodne_cislo, id_zamestnance, dny_dovolene):
        self.jmeno = jmeno
        self.pozice = pozice
        self.rodne_cislo = rodne_cislo
        self.id_zamestnance = id_zamestnance
        self.dny_dovolene = dny_dovolene
frantisek = Zamestnanec("František Novák", "konstruktér", "123", "FN", 25)
klara = Zamestnanec("Klára Nová", "konstruktérka", "123", "KN", 30)
print(frantisek)

