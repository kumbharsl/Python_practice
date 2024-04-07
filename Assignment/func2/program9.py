def outer():
    count = 0
    
    def inner():
        nonlocal count
        count +=1
        return count
    
    return inner

if __name__ == '__main__':
    counter = outer()
    print(counter())
    print(counter())