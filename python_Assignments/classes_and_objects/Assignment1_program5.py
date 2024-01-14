class BCCI:
    
    def __init__(self):
        print('In Constructor: BCCI')
        
    def teams(self):
        print('Teams:-India,Australia.Pakistan')    
        
        
class IPL(BCCI):
    
    def __init__(self):
        print('In Constructor: IPL')
        
    def teams(self):
        print('Teams:-CSK,MI,RCB')
        
obj1=BCCI()
obj1.teams()

obj2=IPL()
obj2.teams()                    