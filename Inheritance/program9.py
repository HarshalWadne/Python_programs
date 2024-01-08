class Demo:
    z=30
    def __init__(self) -> None:
        self._x=10
        self.__y=20
        
obj=Demo()
print(obj.z)
#print(obj.__y)        #Error Instead use-->_Demo__y
print(obj._Demo__y)
print(obj._x)    
print(dir(obj))    