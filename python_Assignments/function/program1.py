#function_Assignments
#program_3
# import array as arr
# def factorial(val):
#     fact=arr.array('i',[])
    
#     for i in range(0,5):
#         x=1        
#         for j in range(i,0,-1):
#             x=x*i
#         fact.append(x)    
#     return fact    
        

# val=arr.array('i', [1,2,3,4])

# print(factorial(val))

# #program_4
# def Parent(digits):
#     def digitCount(digits):
#         count=0
#         for i in len(digits):
#             count+=1
#         print(count)
    
#     def evedigitCount(digits):
#         even=[]
#         for i in digits:
#             if i%2==0:
#                 even.append(i)
#         print(even)    

#     def oddigitCount(digits):
#         odd=[]
#         for i in digits:
#             if i%2==1:
#                 odd.append(i)
#         print(odd)    
#     fun1=digitCount(digits)
#     fun2=evedigitCount(digits)
#     fun3=oddigitCount(digits)
#     return fun1,fun2,fun3


# digits=[1,2,3,4,5,6,7,8,9]
# fun1,fun2,fun3=Parent(digits)
# print(fun1)

#program_5
# class Sum:
#     def mySum(self,number_1,number_2):
#             return number_1+number_2

# obj1=Sum()
# obj2=Sum()

# number1=int(input('enter first number:-'))
# number2=int(input('enter second number:-'))

# x=obj1.mySum(number1,number2)
# y=obj2.mySum(number1,number2)

# total=x+y
# if(total%2==0):
#     print('count is even:-',total)
# else:
#     print('count is odd',total)    

#program_6
# class Department:
#     hOd='xxyyzz'
#     def __init__(self):
#         print('in constructor')
    
#     def division(self):
#         self.div1='alpha'
#         self.div2='beta'
#         self.div3='charlie'
        
    
# obj1=Department()
# obj1.division()
# print(obj1.div1)            
# print(obj1.div2)
# print(obj1.div3)

#program_7
# class Company():
#     def __new__(self):
#         print('in new method')
#         return super().__init__
#     def __init__(self):
#         print('in constructor')
        
        
# obj1=Company()

#program_8
#class IPL:
    