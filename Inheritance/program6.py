class Parent:
    def __init__(self) -> None:
        print("In parent Constructor")
        self.x=10
        self.y=20
        
    def dispParent(self):
        print(self.x)
        print(self.y)
        
        
class Child(Parent):
    def __init__(self) -> None:
        print("IN child Constructor")
        self.x=30
        self.y=40
        super().__init__()            

obj=Child()
obj.dispParent()        