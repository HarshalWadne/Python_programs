class Parent:
    def __init__(self):
        print('In Parent Constructor')
        
    @classmethod    
    def method1(cls):
            print('In class Method ')
            
    @staticmethod        
    def method2():
        print('In Static Method')        
        
    def method3(self):
        print('In Instance Method')    
        
class Child(Parent):
    pass 


obj1=Child()
obj1.method1()
obj1.method2()
obj1.method3()       