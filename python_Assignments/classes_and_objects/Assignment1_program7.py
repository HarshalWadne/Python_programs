class Parent:
    def __init__(self):
        print('In Constructor: Parent')
        
    def __del__(self):
        print("In Destructor: Parent")
        
obj1=Parent()       
obj2= Parent()
obj3=Parent() 
obj4=Parent()
obj1=obj3
del obj2    

