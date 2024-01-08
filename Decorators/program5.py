def gift(func):
    def inner(color):  
    #color=input('which color gift u like:-')
        if(color=='1'):
            print('purple')
            func(color)
        else:
            print('orange')
            func(color)    
    return inner      
    
@gift    
def normal(color):
    print('ur gift')

color='purple'    
normal(color)
