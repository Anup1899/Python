# ------------------------Object Oriented Programming---------------------------------------------------------------
# Four Pillars of OOP
    # 1. Abstraction
    # 2. Encapsulation
    # 3. Inheritance
    # 4. Polymorphism


# Class is a blueprint for creating objects
# Objects are the instance of Classes

class College:
    def __init__(self, college):
        self.college = college

class Student:
    college_name = "XYZ"

    def __init__(self): # Cretated Automtically if not defined by coder
        pass 

    def __init__(self, name): # Constructor --> Invoked automatically whenever the instnace of the class is created
        # Self is refering to the object that has initialized the class
        # It is important to pass self parameter in the constructor
        # It is used to variables belong to the class
        # Data that is stored inside the class are called Attrbutes --> Refering to the Variables
        self.name = name

    def printName(self):
        print(self.name)


student1 = Student("Anup")
student1.printName()


student2 = Student("Aniket")
student2.printName()






print("--------------------------------------Static Methods------------------------")
# Methods in class which does not use self keyword
# Work at class level. Is not linked with object

class Hello:

    def __init():
        pass

    @staticmethod
    def printHello():
        print("Hello")


hello = Hello()
hello.printHello()


# @staticmethod is a Decortor
print("------------------------Decorator-------------------------------")
# Decorator allow us to wrap another function in order to extend the behaviour of wrapped function, without permanantly modifying it
# Decorator takes function as an argument and also return a function


print("------------------------Abstraction-------------------------------")
# Hiding the implementation of details of a class and only showing the essential feature to the user


print("------------------------Encapsulation-------------------------------")
# Wrapping data and function in a single unit (object)
# Class implements Encapsulation

print("------------------------Public/Private-------------------------------")
# By default all the variables and function are Public
# To create any variable private add two underscore in the beginning

class Account:
    def __init__(self, accNo, accPwd):
        self.accountNumber = accNo
        self.__accountPassword = accPwd # Private Attibute --> Can not be accessible outside class

    def __printPassword(self): # Private Method -- Internal Method can access this method
        print(self.__accountPassword) 
    
acc1 = Account("11234", "asc")
print(acc1.accountNumber)
# print(acc1.accountPassword)  # ERROR --> Can not access Private attribute
# print(acc1.__printPassword)  # ERROR --> Can not access Private attribute

print("------------------------Inheritance-------------------------------")
# Accessing the attribute and method of Paremt Class into Child Class

class Car: 
    def __init__(self):
        self.acc = False
        self.brk = True

    def start(self):
        self.acc = True
        self.brk = False
        print("Car Started")

    def stop(self):
        print("Car Stopped")

# Single Level Inheriance
print("----------Single Level----------")
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        

car1 = ToyotaCar("Forutuner")
car1.start()

# Multi-level Inheritance
class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type


print("----------Multi-level----------")
car2 = Fortuner("Fortuner", "Petrol")
print(car2.brand)
print(car2.type)
print(car2.start())

print("----------Multiple----------")
# Inheritance from multiple classes
class A:
    def __init__(self, nameA):
        self.nameA = nameA

class B:
    def __init__(self, nameB):
        self.nameB = nameB

class C(A, B):
    def __init__(self, nameA, nameB, nameC):
        A.__init__(self, nameA)
        B.__init__(self, nameB)
        self.nameC = nameC

name = C("A", "B", "C")
print(name.nameA)
print(name.nameB)
print(name.nameC)

print("----------Super Method ----------")
class B1:
    def __init__(self, b1):
        self.B1 = b1

class C1(B1):
    def __init__(self, C1, B1):
        self.C1 = C1
        super().__init__(B1)

c1 = C1("C", "B")
print(c1.C1)
print(c1.B1)

print("----------Class Method ----------")
# Changing class Arrributes

class Person:
    name = "any"
    age = "-1"

    def  __init__(self, name, age):
        self.name = name
        self.age = age
        # Class Attribute won't change from above
        # self.__class__.name = name # 1. One way of changing the class attributes

    # 2. Second way of changing the class attributes
    @classmethod
    def changeName(cls, name):
        cls.name = name


P1 = Person("Anup", 25)
print(P1.name)
print(P1.age)
print(Person.name, Person.age) 

P1.changeName("ABC")
print(Person.name)

print("----------Property Method ----------")
# Attribute value depend upon the value or calculation
class StudentPerentage:
    def __init__(self, chem, math, phy):
        self.chem = chem
        self.math = math
        self.phy = phy
        self.perentage = str((chem + math + phy)/3) + "%"

    @property # It will recalculate the value if any change of the attribute 
    def calculatePercentage(self): # 
        return str((self.chem + self.math + self.phy)/3) + "%"
    
    # calculatePercentage is not a method it is an attribute

stud = StudentPerentage(97,98,99)
print(stud.perentage) # 98%
print("Property", stud.calculatePercentage) # 98%
stud.phy = 96 
print(stud.perentage) # 98% --> WRONG:- Value is not recalculated
print("Property", stud.calculatePercentage) # 98%



