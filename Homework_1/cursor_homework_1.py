#1
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + ' with age ' + self.age + ' years old is eating.')

    def sleep(self):
        print(self.name + ' with age ' + self.age + ' years old is sleeping.')

    def evolution(self):
        print(self.name + ' with age ' + self.age + ' is evolving now.')


class Dog(Animal):

    def sound(self):
        print(self.name + ' with age ' + self.age + ' years old is barking.')

    def play(self):
        print(self.name + ' with age ' + self.age + ' years old is playing.')


class Cat(Animal):

    def scratch(self):
        print(self.name + ' with age ' + self.age + ' years old is scratching the furniture.')

    def maaay(self):
        print(self.name + ' with age ' + self.age + ' years old is maaaying near the house.')


class Eagle(Animal):

    def looking_for_victim(self):
        print(self.name + ' with age ' + self.age + ' years old is looking for you')

class Wolf(Animal):

    def hunting(self):
        print(self.name + ' with age ' + self.age + ' years old is hunting')

    def deduct(self):
        print(self.name + ' with age ' + self.age + ' years old is deduct to the moon')

class Rabbit(Animal):

    def licking(self):
        print(self.name + ' with age ' + self.age + ' years old is licking grout!')



#1(2)
class Profile:

    def __init__(self,name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        print(self.name + " " + self.last_name + " " + self.phone_number + " " + self.address + " "
              + self.email + " " + self.birthday + " " + self.age + " " + self.sex)


c = Profile("Jaden", "Phillips", '', "Kyiv", "Metakistiv street",'15','2002','male')
c.__str__()


#1a
class Human:

    def __init__(self,name):
        self.name = name


    def eating(self):
        print(self.name + ' have a dinner!')

    def sleep(self):
        print(self.name + ' is sleeping right now!')

    def study(self):
        print(self.name + ' is studying right now!')

    def work(self):
        print(self.name + ' is working right now!')

class Animal:

    def __init__(self, name):
        self.name = name

    def hunting(self):
        print(self.name + ' is hunting')

class Centaur(Human,Animal):

    def evolve(self):
        print(self.name + ' is evolving')

c = Centaur("Grisha")
c.evolve()

#1(3)

from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass


    @abstractmethod
    def webcam(self):
        pass


    @abstractmethod
    def ports(self):
        pass


    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Interface):

    def screen(self):
        print("1920 * 1080")

    def keyboard(self):
        print('Mechanic')

    def touchpad(self):
        print("Adaptive")

    def webcam(self):
        print("10mpx")

    def ports(self):
        print("3 usb ports 3.1 ")

    def dynamics(self):
        print("HP basic dynamics")

laptop = HPLaptop()

laptop.screen()
laptop.keyboard()
laptop.ports()
laptop.touchpad()
laptop.webcam()
laptop.dynamics()





