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
balik = Package("Adresa1", 5)
print(balik.getInfo())
val_package = ValuablePackage("Adresa 2", 3, 1000)
print(val_package.getInfo())
