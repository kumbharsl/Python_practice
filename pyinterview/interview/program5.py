rows  = 5
count = 9
number = 5

for i in range(rows):
    num = count
    for j in range(i):
        print(" ", end="")
    for k in range(i, rows):
        print(num, end=" ")
        num -= 1
    count -= 1
    print()
    
for i in range(rows-2, -1, -1):
    num = number
    for j in range(i):
        print(" ", end="")
    for k in range(i, rows):
        print(num, end=" ")
        num +=1
    print()
    