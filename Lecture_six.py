# def cal_sum (a,b):                                   #Function
#     sum = a + b 
#     print("Sum = ",sum)
#     return sum
# cal_sum(5, 2)
# cal_sum(11, 66)
# cal_sum(100, 677)


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# def cal_sum (a,b):
#     sum = a + b 
#     print(sum)
#     return sum
# cal_sum(a, b)


# def print_h():
#     print("Hello")
# print_h()
# print_h()
# print_h()


# def print_h():        
#     for el in range (0,10):
#      print("Hello")
# print_h()


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter b: "))
# def cal_avg (a,b,c):
#     average = (a + b + c) /3   
#     print(average)
#     return average
# cal_avg(a, b, c)


# def cal_sum (a=1,b=2):                               
#     sum = a + b 
#     print(sum)
#     return sum
# cal_sum()

                               
# def print_len (list) :
#     list = [1,3,5,7,77]
#     print(len(list))
# print_len(list)


# def print_len (list) :
#     list = [1,3,5,7,77]
#     print(list)
# print_len(list)  


# nums = [1,3,5,7,77]
# def print_len (len) : 
#     for item in len:
#      print(item, end=" ")
# print_len(nums)
# print()


# n = int(input("Enter number: "))
# fact = 1
# def print_fact (fact) :
#     for i in range(1,n+1):
#      fact *= i
#     print(fact)
# print_fact(fact)


# n = int(input("Enter number: "))
# def convet_DtoI (n):
#     indrs = 83 * n
#     print(indrs)
# convet_DtoI(n)


# n = int(input("Enter number: "))
# def conveter (n): 
#     if(n%2==0):
#         print("Even")
#     else:
#         print("odd")
# conveter(n)


# def show(n):                                         #Recursion
#     if(n == 0):
#           return
#     print(n)  
#     show(n-1)
# show(5)       


# def cal(a,b):
#     s=a*b
#     print(s)
#     return s
# cal(3,6)
# cal(6,8)







import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

gcd = math.gcd(a, b)

print(f"The GCD of {a} and {b} is: {gcd}")
