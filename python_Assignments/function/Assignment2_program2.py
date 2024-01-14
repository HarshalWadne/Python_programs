#program_2
# def outer():
#     def inner():
#         return "Hello I'm in Inner Function"
    
#     return inner()

# retObj=outer()
# retInner=retObj()
# print(retInner)

def outer():
    def inner():
        return "Greetings from the Inner Function"
    
    return inner()


if __name__=="__main__":
    result=outer()
    print(result)