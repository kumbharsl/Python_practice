def print_pattern(n):
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Increasing sequence from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Decreasing sequence from (i-1) back to 1
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        # Move to the next line
        print()

# Test with n = 7
print_pattern(7)
