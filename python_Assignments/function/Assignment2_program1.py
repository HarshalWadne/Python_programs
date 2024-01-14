#program_1
# def outer():
#     def inner():
#         return "Hello, I am in Inner function"
#     return inner()

# ans=outer()
# print(ans)    
# print(type(__name__))

def add(x):
    def inner(y):
        return x*y
    return inner

if __name__=='__main__':
    add_3=add(3)
    result=add_3(7)
    print(result)
