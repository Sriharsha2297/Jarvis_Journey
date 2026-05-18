# Error Handling
# n try / except / finally blocks
# n Specific: ValueError, FileNotFoundError, ZeroDivisionError
# n raise ValueError('Invalid input')
# n Add error handling to calculator
# n Handle invalid input gracefully

History = []

def calculator():
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Zero division error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Calculator session ended.")

    History.append(f"{num1} {operation} {num2} = {result}")

# calculator()

# __name__ == "__main__" is a common Python idiom that checks if the script is being run directly (as the main program) rather than imported as a module. 
# If the condition is true, it executes the code block under it. 
# This allows you to have code that only runs # when the script is executed directly, and not when it's imported elsewhere.    
if __name__ == "__main__":
    calculator()