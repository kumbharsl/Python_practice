def outer():
    def inner():
        return outer
    
    return inner

if __name__ == '__main__':
    retObj = outer()
    retInner = retObj()
    print(retInner)