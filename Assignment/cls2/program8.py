class Demo:
    def __init__(self):
        print("In Constructor")
        
    def __del__(self):
        print("In Destructor")
        
def Fun():
    print("In fun")
    obj = Demo()
    print("End fun")
    return obj

Fun()
