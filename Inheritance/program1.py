class Demo:
    def __init__(self):
        print('constructor')
        self.x=10
        self.y=20
        
    def setData(self,z):
        self.z=z
        
    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z)
        
        
obj1=Demo()     
obj1.printData() #Attributr Error 