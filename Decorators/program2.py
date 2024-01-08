def outer():
    def innner():
        print("in inner")
        
    print("in outer")
    return innner

ret=outer()
ret()    