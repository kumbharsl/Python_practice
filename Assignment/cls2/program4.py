class Parent:
    def __init__(self):
        pass
    
    @classmethod
    def cls(self):
        print("In Class Method")
        
    @staticmethod
    def static():
        print("In Static Method")
    
class Child(Parent):
    def __init__(self):
        print('In Constructor')
    
obj1 = Child()
obj1.cls()
Parent.static()
    