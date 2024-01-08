#function Decorators.....

def decorFun(fun):
    def inner():
        print("Start Decorator")
        fun()
        print("End Decorator")
    return inner    
        
    
@decorFun    
def normalFunc():
    print("hello i am in Normal Func")
    
normalFunc()
       
    