def outer():
    def inner():
        return "Hello, I'm the inner fucntion!"
    return inner()

ans = outer()
print(ans)