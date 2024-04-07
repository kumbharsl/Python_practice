row = int(input("Enter the row : "))
k = 0
for i in range(row):
    for j in range((row-i)+1):
        print(end = " ")
    while k!=(i+1):
        print("*", end = " ")
        k+=1
    k=0
    print()