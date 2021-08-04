class Package:
    def getInfo(self):
        return f"Balík je na adresu {self.address}, váží {self.weightInKilos} kg a stav doručení je {self.delivered}"
    def deliver(self):
        self.delivered = True
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False
class ValuablePackage(Package):
    def __init__(self, address, weightInKilos, value):
        self.value = value
        super().__init__(address, weightInKilos)
class Driver:
    def zbyva_baliku(self):
        pocet_baliku = 0
        for polozka in self.seznam_baliku:
            if polozka.delivered == False:
                pocet_baliku = pocet_baliku + 1
        return pocet_baliku
    def prirad_balik(self, balik):
        # self.seznam_baliku = self.seznam_baliku + list(args)
        if balik.delivered == True:
            print("Balík již byl doručen.")
        else:
            self.seznam_baliku.append(balik)
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.seznam_baliku = []
balik1 = Package("Adresa 1", 30)
balik2 = ValuablePackage("Adresa 2", 5, 100)
ridic = Driver("Jirka")
ridic.prirad_balik(balik1)
ridic.prirad_balik(balik2)
print(ridic.zbyva_baliku())
balik1.deliver()
print(ridic.zbyva_baliku())