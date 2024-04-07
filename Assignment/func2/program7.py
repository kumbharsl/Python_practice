def outer():
    def inner():
        return "Hello, Core2web!"
    return inner
    print("In outer Function")

if __name__ == '__main__':
    result = outer() ()
    print(result)