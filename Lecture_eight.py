# class Student :
#     name = "Deepak"
# s1 = Student()
# print(s1.name)
# print(s1)
# s2 = Student()
# print(s2.name)


# class Student :
#     name = "Deepak"
#     def __init__(self):                                # line --  (Constructor) 
#         print("Addiing new data in database")
# s1 = Student()


# class Student :  
#     def __init__(self, fullname,marks):
#         self.name = fullname
#         self.name = marks
#         print("Addiing new data in database")
# s1 = Student("Deepak kumar", 93)
# print(s1.name)


class Student :  
    # default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Addiing new data in database")
s1 = Student("Deepak kumar", 93)
print(s1.name, s1.marks)


# class Student :  
#     college_name = "IILM"
#     def __init__(self, fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("Addiing new data in database")
# s1 = Student("Deepak kumar", 93)
# print(s1.name,s1.marks)
# print(s1.college_name)
# s2 = Student("Deepak", 73)
# print(s2.name,s2.marks)
# print(s2.college_name)


# class Student :  
#     college_name = "IILM"
#     def __init__(self, fullname,marks):
#         self.name = fullname
#         self.marks = marks
#     def welcome (self):
#             print("Welcome student", s1.name, s1.marks)
# s1 = Student("Deepak kumar", 93)
# s1.welcome()


# class Student :  
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#     def get_avg (self):
#         sum = 0
#         for val in self.marks:
#            sum += val
#         print("Hello", self.name, "Your score is:",sum/3)
# s1 = Student("Deepak Kumar", [93,77,78])
# s1.get_avg()
# s1.name = "PK"
# s1.get_avg()


# class car:                                          # EX of Abstraction 
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False
#     def start (self):
#         self.clutch = True
#         self.accelerator = True
#         print("Car started")
# car1 = car()
# car1.start()


# class account:                                                 # practice question
#     def __init__(self,balance, accountno):
#         self.balance = balance
#         self.accountno = accountno
#         # debit method 
#     def debit (self, amount):
#             self.balance -= amount
#             print("Rs", amount, "was Debited")
#             print("Total balance =", self.get_balance())
#         # Credit method
#     def credit (self, amount):
#             self.balance += amount
#             print("Rs", amount, "was Credited")
#             print("Total balance =", self.get_balance())
#     def get_balance(self):
#         return self.balance
# a1 = account(2000, 4451182100)
# print("Before Debit and Credit Total balance = ",a1.balance)
# a1.debit(1000)
# a1.credit(500)