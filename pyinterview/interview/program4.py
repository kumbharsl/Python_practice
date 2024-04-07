class Number:
    @staticmethod
    def main():
        rows = 4
        # Upper part of the pattern
        for i in range(rows):
            # Print spaces before numbers
            print(" " * (2 * (rows - i - 1)), end="")
            # Print ascending numbers
            for j in range(1, i + 2):
                print(j, end=" ")
            # Print descending numbers
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()
        space = 7
        # Lower part of the pattern
        for i in range(rows):
            # Print spaces before numbers
            print(" " * (space * 2), end="")
            # Print ascending numbers
            for j in range(1, rows - i + 1):
                print(j, end=" ")
            # Print descending numbers
            for j in range(rows - i - 1, 0, -1):
                print(j, end=" ")
            space += 1
            print()  # Move to the next line after each row
if __name__ == "__main__":
  Number.main()
