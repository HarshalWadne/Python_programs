class Demo:
    def __init__(self) -> None:
        print("IN constructor")
        
    def __del__(self):
        print("IN destrcutor")
        
        
def func():
    print("Start Fun")
    obj=Demo()
    print("End Fun")            
    
    
func()
print("End Code")    