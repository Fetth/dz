class Book():

    def __init__(self, name, year, producer, janr, autor, cost):
        self.name = name
        self.year = year
        self.producer = producer
        self.janr = janr
        self.autor = autor
        self.cost = cost
# set свойства
    def setName(self):
        self.name = input("название книги ")
    def setyear(self):
        self.year = input("год выпуска ")
    def setproducer(self):
        self.producer = input("издатель ")
    def setjanr(self):
        self.janr = input("жанр ")
    def setautor(self):
        self.autor = input("автора ")
    def setCost(self):
        self.cost = input("цену ")

    def setAll(self):
        self.name = input("название книги ")
        self.year = input("год выпуска ")
        self.producer = input("издатель ")
        self.janr = input("жанр ")
        self.autor = input("автора ")
        self.cost = input("цену ")

# get свойства
    def getname(self):
        print(self.name)
    def getryear(self):
        print(self.year)
    def getproducer(self):
        print(self.producer)
    def getjanr(self):
        print(self.janr)
    def getautor(self):
        print(self.autor)
    def getcost(self):
        print(self.cost)

    def out(self):
        print(self.name)
        print(self.year)
        print(self.producer)
        print(self.janr)
        print(self.autor)
        print(self.cost)
I = Book("", "", "", "", "", "")
I.out()
I.setAll()
I.out()
I.setName()
I.out()
I.setyear()
I.out()
I.setproducer()
I.out()
I.setjanr()
I.out()
I.setautor()
I.out()
I.setCost()
I.out()
