def outer():
    def inner():
        return "Greetings from the inner Function"
    
    return inner

if __name__=='__main__':
    retObj=outer()
    retInner=retObj()
    
    print(retInner)