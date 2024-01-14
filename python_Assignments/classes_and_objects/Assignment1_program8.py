class MI:
    
    def __init__(self) -> None:
        print('In Constructor: MI')
        
    @classmethod
    def method1(captain):
        print('Captain:ROHIT SHARMA')
        
    @staticmethod
    def method2():
        print("Franchise :MI")
        
    def method3(self):
           print('Team Members:-Hardik Pandya,Surya')     
           
obj1=MI()
obj1.method1()
obj1.method2()
obj1.method3() 