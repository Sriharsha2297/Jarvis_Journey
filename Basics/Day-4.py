# Build calculator: takes two numbers and an operator
# Support: + - * /
# Handle division by zero
# Loop until user types 'quit'
# BONUS: square root and power

def calculator(int1, int2, operator):
    if operator == '+':
        return int(int1) + int(int2)
    elif operator == '-':
        return int(int1) - int(int2)
    elif operator == '*':
        return int(int1) * int(int2)
    elif operator == '/':
        if int(int2) == 0:
            return "Error: Division by zero is not allowed."
        else:
            return int(int1) / int(int2)
    elif operator == 'sqrt':
        return f"Square root of {int1} is {int(int1)**0.5} and square root of {int2} is {int(int2)**0.5}"
    elif operator == 'power':
        return f"{int1} raised to the power of {int2} is {int(int1)**int(int2)}"
    else:
        return "Invalid operator. Please use +, -, *, /, sqrt, or power."



print("Welcome to the calculator! Type 'quit' to exit.")
while True:
    User_Input = input (" Enter 2 numbers (x, y) that you wamt to use math opperators on : ")
    if User_Input.lower() == 'quit':
        print("Exiting the calculator. Goodbye!")
        break
    Temp = User_Input.split(",")
    int1, int2 = Temp[0], Temp[1]
    operator = input("Enter an operator (+, -, *, /, sqrt, power): ")
    Result = calculator(int1, int2, operator)
    print(f"Result: {Result}")