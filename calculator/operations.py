# def add(x,y):
#     return x + y

# def subtract(x,y):
#     return x - y

# def multiply(x,y):
#     return x * y

# def divide(x,y):
#     return x / y
from decimal import Decimal
# Define the functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b