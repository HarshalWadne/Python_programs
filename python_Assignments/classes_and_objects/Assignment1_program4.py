class Parent:
    def __init__(self,age,name):
        print("In constructor :Parent")
        self.age=age
        self.name=name
        
    def method1(self,age,name):
        print('age:-',age)
        print('name:-',name)
        
class Child(Parent):
    def __init__(self):
        print('In Constructor: Child')
        

obj1=Child()
obj1.method1(21,'Harshal')
                    
        
        