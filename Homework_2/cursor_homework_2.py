import random

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Person:
    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def introduce_about_yourself(self):
        print(f"Hi. My name is {self.name}, and I'm {self.age}'\n\'")
        print(f"I have {self.money} in my bank account'\n\'")
        if self.house != False:
            print(f"I have a house with area {house.area}")
        else:
            print(f"I don't have a house")

    def make_money(self, working):
        self.money += working
        print(f"From this moment I have {self.money}")


    def buy_the_house(self, home):
        if self.money >= home.cost:
            self.money -= home.cost
            self.house = True
            print(f"I have bought the house with {home.area}m^2 and price:{home.cost}")
        else:
            print(f"I don't have enough money for purchase this house")



class House:
    def __init__(self,area,cost):
        self.area = area
        self.cost = cost


    def apply_discount(self, house_discount):
        self.cost *= (100 - house_discount) / 100
        print(f"The price of the house with discount will be: {self.cost}")



class Rieltor(metaclass=SingletonMeta):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info(self):
        print(f"My name is {self.name}")
        for r,houses in enumerate(self.houses):
            print(f"{r+1} This house has area: {houses.area} with price: {houses.cost}")



    def give_discount(self,house):
        house.apply_discount(self.discount)


    def steal(self,somebody):
        r = random.randrange(0,100)
        if r <= 10:
            somebody.money = 0
            print(f"The Rieltor stole all your money")
        else:
            print(f"The Rieltor tryied to steal your money")



person = Person("Alex", "20", 5000, False)
person.introduce_about_yourself()
person.make_money(14000)

house = House(25, 10000)
house_1 = House(50, 20000)
houses = [house, house_1]

rieltor = Rieltor("Fedor", houses, 15)
rieltor.provide_info()
rieltor.give_discount(house_1)
person.buy_the_house(house_1)