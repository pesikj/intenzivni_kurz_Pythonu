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
    def pridej_podrizeneho(self, podrizeny):
        self.podrizeni.append(podrizeny)
    def zjisti_podrizene(self):
        podrizeni = "Podřízení jsou: "
        for polozka in self.podrizeni:
            podrizeni = podrizeni + polozka.jmeno + ", "
        return podrizeni
    def __str__(self):
        text = super().__str__()
        text = text + f" Má {len(self.podrizeni)} podřízených."
        return text
    def __init__(self, jmeno, pozice, zkusebni_doba):
        super().__init__(jmeno, pozice, zkusebni_doba)
        self.podrizeni = []
frantisek = Zamestnanec(pozice="konstruktér", jmeno="František Novák", zkusebni_doba=True)
klara = Zamestnanec("Klára Nová", "konstruktérka", False)
marian = Manazer("Marian Přísný", "vedoucí KO", False)
marian.pridej_podrizeneho(frantisek)
marian.pridej_podrizeneho(klara)
print(marian.zjisti_podrizene())

