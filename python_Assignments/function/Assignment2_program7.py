def outer():
    def inner():
        return "Hello ,Core2web"
    return inner
    print("In Outer Function")  #Code will not reach till here
    
if __name__=='__main__':
    result=outer()()
    print(result)    