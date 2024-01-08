class Parent:
    def __init__(self) -> None:
        print('Parent Constructor')
        
    def parentFunc(self):
        print('In parent function')
        
class Child(Parent):
    def __init__(self):
        print('In child Constructor')
        
    def childFunc(self):
        print('In Child function')    
obj1=Child()
obj1.parentFunc()     
obj1.childFunc()           