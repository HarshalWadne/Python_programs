class Parent:
    def __init__(self) -> None:
        print('In Parent Constructor')
    
    def parentFunc(self):
        print('In Parent Function')
        
        
class Child(Parent):
    def __init__(self):
        super().__init__() 
        print('In Parent Constructor')
    
    def childFunc(self):
        print('In Child function')
        
        
obj1=Child()
obj1.parentFunc()
obj1.childFunc()         
print(id(Parent.__init__))   
print(id(Child.__init__)) 