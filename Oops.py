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
