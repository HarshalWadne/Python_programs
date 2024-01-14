class Human:
    def __init__(self,name,age):
        print("In Human Constructor")
        self.age=age
        self.name=name
        
    def information(self):
        print('name is',self.name)
        print('age is',self.age)
        
name=input("Enter name:-")
age=int(input("Enter your age:-"))

if __name__=='__main__':
    obj1=Human(name,age)
    obj1.information()