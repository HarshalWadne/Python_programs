class Main:
    
    def __init__(self):
        print('In Constructor: Main')
        
class A(Main):
    def __init__(self):
        print("In Constructor: A") 
        
class B(A):
    def __init__(self):
        print('In Constructor: B')
   
class C(A):
    def __init__(self):
        print("In Constructor: C")       
        
class D(B,C):
    def __init__(self):
        print("In Constructor: D")       
        
class E(D):
    def __init__(self):
        print("In Constructor: E")         
        

obj1=E()                        
print(E.__mro__)                       