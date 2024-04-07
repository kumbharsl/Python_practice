def outer():
    def inner():
        return "This is the inner function."
    return inner

if __name__ == '__main__' :
    retObj = outer()
    retInner = retObj()
    
    print(retInner)