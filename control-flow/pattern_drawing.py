# pattern_drawing.py

# Prompt user for the size of the pattern
size_input = input("Enter the size of the pattern: ")

# Try to convert to integer
try:
    size = int(size_input)
except ValueError:
    print("Please enter a valid integer next time.")
    exit()

# Ensure it's positive
if size <= 0:
    print("Size must be a positive integer.")
    exit()

# Use a while loop for rows
row = 0
while row < size:
    # Use a for loop for columns in the current row
    for _ in range(size):
        print("*", end="")
    print()  # newline after each row
    row += 1
