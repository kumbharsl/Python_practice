def outer():
    def inner():
        return "Hello,I'm the inner function!"

    return inner

retObj = outer()
retInner = retObj()

print(retInner)