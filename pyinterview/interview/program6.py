number = 1
n = 1
space = 3
secondNumber = 1
secondSpace = 7
for i in range(8):
    count = n
    if i < 4:
        print("  " * space, end='')
        for j in range(1, number + 1):
            print(count, end=' ')
            count += 1
        number += 2
        space -= 1
        print()
    else:
        print("  " * secondSpace, end='')
        for j in range(1, secondNumber + 1):
            print(count, end=' ')
            count += 1
        secondNumber += 2
        secondSpace -= 1
        print()