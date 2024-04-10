row=9
for i in range(row):
    num=row-i
    for j in range(row-i):
        if num==9:
            print("6",end=" ")
        elif num==6:
            print("9",end=" ")
        else:
            print(num,end=" ")
        num-=1
    print()