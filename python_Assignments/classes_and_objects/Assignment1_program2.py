class Vehicle:
    def __init__(self,brand,model,year,speed):
        print('In Constructor Vehicle')
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
        
    def accelerate(self):
        print('In method accelerate: Vehicle')
        
    def brake(self):
        print("In method brake: Vehicle")      
        
    def honk(self):
        print("In Method Honk: Vehicle")
        
        
class vehicleChild():
    
    def __init__(self,brand,model,year,speed):
        print('In Constructor vehicleChild')
        super().__init__
    
    def accelerate(self):
        print('In Method Accelerate: vehicleChild')
        
    def honk(self):
        print('In Method Accelerate: vechileChild')
        
obj1=Vehicle('BMW','i5',2010,300)
obj2=vehicleChild('BMW','i5',2010,300)                          
        
        