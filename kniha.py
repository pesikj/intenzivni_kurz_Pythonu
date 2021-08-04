class Book:
    def discount(self, discount):
        self.price = int(self.price * (1 - discount / 100))
    def getInfo(self):
        text = f"Kniha {self.title} má {self.pages} a její cena je {self.price}"
        return text
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

book1 = Book("Testovací kniha", 1000, 500)
print(book1.getInfo())
book1.discount(10)
print(book1.getInfo())

