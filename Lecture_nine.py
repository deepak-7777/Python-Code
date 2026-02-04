# class student :
#     def __init__(self, name):
#         self.name = name
# s1 = student("deepak")
# s2 = student("ram")
# del s1.name                                # using delet syntax
# print(s2.name)
# print(s1.name)                              # Attribute error , because delete syntax are used.


# class account :
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
# acc1 = account("1234", "asdf")
# print(acc1.acc_no)
# print(acc1.acc_pass)                          # password are public 


# class account :
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass                # using line (__)  After password are private 
#     def reset_pass (self) :                          # and using the reset 
#         print(self.__acc_pass)
# acc1 = account("1234", "asdf")
# print(acc1.acc_no)
# print(acc1.reset_pass())
# print(acc1.acc_pass)               #Attribute error , because used this (__)  syntax


# class student : 
#     def __hello():             #Attribute error , because used this (__)  syntax
#         print("hello")
# s1 = student()
# print(s1.hello) 
  

# class car:                                # Ex. of Inheritance   (Single inheritance)
#     @staticmethod
#     def start ():
#         print("Car Started..")
#     @staticmethod
#     def stoped ():
#         print("Car Stoped..")           
# class toyotacar(car):
#     def __init__(self, name):
#         self.name = name
# car1 = toyotacar("fortuner")
# car2 = toyotacar("Prius")
# print(car1.name)
# print(car2.name)
# print(car1.start())


# class car:                                       # Multi-level inheritance
#     @staticmethod
#     def start ():
#         print("Car Started..")
#     @staticmethod
#     def stoped ():
#         print("Car Stoped..")           
# class toyotacar(car):
#     def __init__(self, brand):
#         self.brand = brand
# class fortuner(toyotacar):
#     def __init__(self, type):
#         self.type = type
# car1 = fortuner("diesel")
# print(car1.type)
# car1.start()


# class A:                                        #  Multiple inheritance
#     variable1 = "Welcome to class A"
# class B:
#     variable2 = "Welcome to class B"
# class C(A, B):
#     variable3 = "Welcome to class C"
# c1 = C()
# print(c1.variable1)
# print(c1.variable2)
# print(c1.variable3)


# class car:        
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start ():
#         print("Car Started..")
#     @staticmethod
#     def stoped ():
#         print("Car Stoped..")           
# class toyotacar(car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)                # Use super method
# car1 = toyotacar("prius", "electric")
# print(car1.type)
# car1.start()


# class person:
#     name = "Rahul"
#     def changedname (self, name):
#          person.name = name
# p1 = person()
# p1.changedname("Deepak")
# print(p1.name)
# print(person.name)
# print(person)


# class person:
#     name = "Rahul"
#     @classmethod
#     def changedname(cls, name):
#         cls.name = name
# p1 = person()
# p1.changedname("Deepak")
# print(p1.name)
# print(person.name)


# class Student:
#     def __init__(self, phy, chem, math):
#       self.phy = phy
#       self.chem = chem
#       self.math = math
#       self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
#     def calcPercentage(self):
#        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)
# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property                                                                # used Property 
#     def percentage(self):  # Changed 'Percentage' to 'percentage'
#         return str((self.phy + self.chem + self.math) / 3) + "%"
# stu1 = Student(98, 97, 99)
# print(stu1.percentage) 
# stu1.phy = 86
# print(stu1.percentage)
                                                                 #  Implementation Of Polymorphism


# class Complex:                                       # Add
#   def __init__(self, real, img):
#     self.real = real
#     self.img = img
#   def showNumber(self):
#     print(self.real, "i +", self.img, "j")
#   def __add__(self, num2):                               # Used Dunder function
#     newReal = self.real + num2.real
#     newImg = self.img + num2.img
#     return Complex(newReal, newImg)
# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 6)
# num2.showNumber()
# num3 = num1 + num2
# num3.showNumber()


# class Complex:                                                # Subtract
#   def __init__(self, real, img):
#     self.real = real
#     self.img = img
#   def showNumber(self):
#     print(self.real, "i +", self.img, "j")
#   def __sub__(self, num2):                               # Used Dunder function
#     newReal = self.real - num2.real
#     newImg = self.img - num2.img
#     return Complex(newReal, newImg)
# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 6)
# num2.showNumber()
# num3 = num1 - num2
# num3.showNumber()

                                                  # Q.No 1
# class Circle:
#   def __init__(self, radius):
#     self.radius = radius
#   def area(self):
#     return (22/7) * self.radius ** 2
#   def perimeter(self):
#     return 2 * (22/7) * self.radius
# c1 = Circle(21)
# print("Area = ",c1.area())
# print("perimeter = ",c1.perimeter())


                                                # Q.No 2
# class Employee:
#   def __init__(self, role, dept, salary):
#     self.role = role
#     self.dept = dept
#     self.salary = salary
#   def showDetails(self):
#     print("role =", self.role)
#     print("dept =", self.dept)
#     print("salary =", self.salary)
# class Engineer(Employee):
#       def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Elon Musk", 40) 
# engg1.showDetails()



                                                # Q.No 3
class Order:
  def __init__(self, item, price):
    self.item = item
    self.price = price

  def __gt__(self, odr2):
    return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)
print(odr1 > odr2)