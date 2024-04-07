row = int(input("Enter the row : "))

num = 9
for i in range(row):
    for j in range(row-i):
        print(num-1,end=" ")
        #num -= 1
    print()
    num -=1