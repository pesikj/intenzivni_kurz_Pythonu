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
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.__dny_dovolene = 25
        self.zkusebni_doba = zkusebni_doba
frantisek = Zamestnanec(pozice="konstruktér", jmeno="František Novák", zkusebni_doba=True)
#klara = Zamestnanec("Klára Nová", "konstruktérka", "123", "KN", 30, False)
print(frantisek)
frantisek.__dny_dovolene = 50
print(frantisek.__dny_dovolene)
#print(klara)

