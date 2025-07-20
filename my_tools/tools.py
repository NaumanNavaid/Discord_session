from agents import function_tool

@function_tool
def add(a: int, b: int) -> int:
    print("add")
    """Adds two integers."""
    return a + b

@function_tool
def subtract(a: int, b: int) -> int:
    print("subtract")
    """Subtracts the second integer from the first."""
    return a - b

@function_tool
def multiply(a: int, b: int) -> int:
    print("multiply")
    """Multiplies two integers."""
    return a * b

@function_tool
def divide(a: int, b: int) -> float:    
    print("divide")
    """Divides the first integer by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b