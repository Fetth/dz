class stadium():

    def __init__(self, name, year, country, city, mesta):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.mesta = mesta

    # set свойства
    def setName(self):
        self.name = input("название стадиона ")

    def setyear(self):
        self.year = input("дату открытия ")

    def setcountry(self):
        self.country = input("страну ")

    def setcity(self):
        self.city = input("город ")

    def setmesta(self):
        self.mesta = input("вместимость ")

    def setAll(self):
        self.name = input("название стадиона ")
        self.year = input("дату открытия ")
        self.country = input("страну ")
        self.city = input("город ")
        self.mesta = input("вместимость ")

    # get свойства
    def getname(self):
        print(self.name)
    def getryear(self):
        print(self.year)
    def getcountry(self):
        print(self.country)
    def getcity(self):
        print(self.city)
    def getmesta(self):
        print(self.mesta)

    def out(self):
        print(self.name)
        print(self.year)
        print(self.country)
        print(self.city)
        print(self.mesta)


I = stadium("", "", "", "", "")
I.out()
I.setAll()
I.out()
I.setName()
I.out()
I.setyear()
I.out()
I.setcountry()
I.out()
I.setcity()
I.out()
I.setmesta()
I.out()
