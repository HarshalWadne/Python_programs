def decorRun(func):
    def wrapper():
        print('Start Wrapper1')
        func()
        print("End wrapper1")
       
    return wrapper

def decorFun(func):
    def wrapper():
        print('Start Wrapper2')
        func()
        print("End wrapper2")
        
    return wrapper

@decorRun
@decorFun
def normalFunc():
    print('in Normal func')
    
normalFunc()  