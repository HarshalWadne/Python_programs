class TATA:
    def __init__(self):
        print('In Constructor: TATA')
        
    def owner(self):
        print('Ratan Tata')    
        
class TCS(TATA):
    
    def __init__(self):
        print('IN Constructor: TCS')
        
obj1=TCS()
obj1.owner()                