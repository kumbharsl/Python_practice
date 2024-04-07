rows = 4
    # Upper part of the pattern
for i in range(rows):
        # Print spaces before numbers
    print(" " * (2 * (rows - i - 1)), end="")
        # Print ascending numbers
    for j in range(1, i + 2):
        print(j, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    # Lower part of the pattern
for i in range(rows):
        # Print spaces before numbers
    print(" " * (2 * i), end="")
        # Print ascending numbers
    for j in range(1, rows - i + 1):
        print(j, end=" ")
        # Print descending numbers
    for j in range(rows - i - 1, 0, -1):
        print(j, end=" ")
    print()