# calculator.py

def add(a: int | float, b: int | float) -> int | float:
    """Returns the sum of a and b."""
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Returns a minus b."""
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    """Returns a multiplied by b."""
    return a * b

def divide(a: int | float, b: int | float) -> float:
    """Returns a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

