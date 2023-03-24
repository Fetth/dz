import Book
import Stadium


class Avtomobile():

    def __init__(self, name, year, produce, engine, color, cost):
        self.name = name
        self.year = year
        self.produce = produce
        self.engine = engine
        self.color = color
        self.cost = cost
# set свойства
    def setName(self):
        self.name = input("Введите название автомобиля ")
    def setyear(self):
        self.year = input("Введите год производства автомобиля ")
    def setproduce(self):
        self.produce = input("Введите название производителя ")
    def setengine(self):
        self.engine = input("Введите объем двигателя ")
    def setColor(self):
        self.color = input("Введите цвет автомобиля ")
    def setCost(self):
        self.cost = input("Введите цену автомобиля ")

    def setAll(self):
        self.name = input("Введите название автомобиля ")
        self.year = input("Введите год производства автомобиля ")
        self.produce = input("Введите название производителя ")
        self.engine = input("Введите объем двигателя ")
        self.color = input("Введите цвет автомобиля ")
        self.cost = input("Введите цену автомобиля ")

# get свойства
    def getname(self):
        print(self.name)
    def getryear(self):
        print(self.year)
    def getproduce(self):
        print(self.produce)
    def getengine(self):
        print(self.engine)
    def getcolor(self):
        print(self.color)
    def getcost(self):
        print(self.cost)

    def out(self):
        print(self.name)
        print(self.year)
        print(self.produce)
        print(self.engine)
        print(self.color)
        print(self.cost)
I = Avtomobile("Paid", "2020", "Teals", "Electro", "Black", "5000000")
I.out()
I.setAll()
I.out()
I.setName()
I.out()
I.setyear()
I.out()
I.setproduce()
I.out()
I.setengine()
I.out()
I.setColor()
I.out()
I.setCost()
I.out()
