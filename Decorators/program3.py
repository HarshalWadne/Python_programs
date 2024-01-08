def decorFun(func):
    def wrapper(*args):
        print('Start Wrapper')
        val=func(*args)
        print("End wrapper")
        return val
    
    return wrapper

@decorFun
def normalFunc():
    print('in Normal func')
    
normalFunc()    