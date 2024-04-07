def outer():
    def inner():
        return "Hello, I'm the inner fucntion!"
    
    return inner 

retObj = outer()
retInner = retObj

print(retInner)