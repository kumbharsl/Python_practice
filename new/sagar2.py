def print_diagonal_pattern(n):
    # Create an empty matrix with empty strings for formatting
    matrix = [['' for _ in range(n)] for _ in range(n)]
    
    num = 1  # Start number
    
    # Fill the matrix diagonally
    for col in range(n):
        i = 0
        j = col
        while j >= 0:
            matrix[i][j] = str(num)  # Store numbers as strings for proper formatting
            num += 1
            i -= 1
            j -= 1
            
    # Continue filling the matrix for the remaining rows
    for row in range(1, n):
        i = row
        j = n - 1
        while i < n:
            matrix[i][j] = str(num)
            num += 1
            i += 1
            j -= 1

    # Print the matrix in the desired staggered pattern
    for row in range(n):
        for col in range(n):
            if matrix[row][col] != '':  # Only print non-empty cells
                print(matrix[row][col], end=" ")
        print()

# Test the function with n = 5
print_diagonal_pattern(5)
