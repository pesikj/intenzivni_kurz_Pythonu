class Package:
    def getInfo(self):
        self.deliver()
        return f"Balík je na adresu {self.address}, váží {self.weightInKilos} kg a stav doručení je {self.delivered}"
    def deliver(self):
        self.delivered = True
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False
balik = Package("Adresa1", 5)
balik.deliver()
print(balik.getInfo())
