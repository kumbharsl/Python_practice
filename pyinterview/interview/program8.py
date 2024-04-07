 '''      *
        * *
      * * *
    * * * *
  * * * * *     '''
row = int(input("Enter the row : "))

for i in range(row):
    num = i+1
    for j in range(row-i):
        print(" ", end = " ")
    for k in range(i+1):
            print("*" ,end= " ")
    print()