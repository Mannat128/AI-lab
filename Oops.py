"""
class student :
    pass
student1 = student()
student2 = student()
print(student1)
print(student2)
"""
"""
#Constructor
class student:
    def __init__(self):
        print("student created")
s1 = student()
print(s1)
"""
'''
#Attributes(variable inside class)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1 = student("Mannat",21)
print(s1.name)
print(s1.age)
'''
'''
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is ",self.name)
    def ages(self):
        print("My age is ",self.age)
s1 = student("Mannat",21)
s1.introduce()
s1.ages()
'''
'''
#Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
        print("balance: ",self.__balance)
account = BankAccount(25000)
account.show_balance()
'''
'''
#Inheritance
# 1.Single inheritance
class Animal:
    def eat (self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("dog is barking")
d = Dog()
d.eat()
d.bark()
'''
'''
#2. Multilevel 
class grandfather:
    def house(self):
        print("House")
class father(grandfather):
    pass
class son(father):
    pass
s = son()
s.house()
'''
'''
# 3. Multiple
class father:
    def skill1(self):
        print("Driving")
class mother:
    def skill2(self):
        print("Cooking")
class child(father,mother):
    pass
c = child()
c.skill1()
c.skill2()
'''
'''
# Polymorphism
class dog:
    def sound (self):
        print("bark")
class cat:
    def sound (self):
        print("meow")
class monkey:
    def sound (self):
        print("cha cha")

animals = [dog(),cat(),monkey()]
for animal in animals:
    animal.sound()
'''
'''
# Abstraction
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started")
c = car()
c.start()
'''
'''
# Super()keyword
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id = id
s = student("Mannat",101)
print(s.name)
print(s.id)
'''
'''
# practical example
class employee:
    company = "corptube"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")

class developer(employee):
    def __init__(self, name, salary,tech):
        super().__init__(name, salary)
        self.tech = tech
    def display(self):
        super().display()
        print(f"tech: {self.tech}")
s1 = developer("Mannat",45000,"Prompt Engineer")
s1.display()
print(s1.company)
'''

