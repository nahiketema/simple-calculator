# A simple calculator program

# Part 1: Get user input
# Get the first number, making sure to convert the input string to a number (float).
num1_str = input("Enter the first number: ")
num1 = float(num1_str)

# Get the operation symbol.
operator = input("Enter an operation (+, -, *, /): ")

# Get the second number.
num2_str = input("Enter the second number: ")
num2 = float(num2_str)

# Part 2: Perform the calculation based on the operator
result = 0

# Use an if-elif-else block to check the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Check for division by zero to prevent errors
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    # Handle an invalid operator
    print("Error: Invalid operator entered.")

# Part 3: Print the result
# Only print the result if a valid operation was performed.
if operator in ['+', '-', '*', '/'] and num2 != 0:
    print(f"Result: {num1} {operator} {num2} = {result}")
