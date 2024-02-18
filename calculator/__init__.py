# def add(x,y):
#   return x + y

# def subtract(x,y):
#   return x - y

# def multiply(x,y): 
#   return x * y

# def divide(x,y):   
#   return x / y

# def exponential(x,y):
#     return x**y
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(x,y):
        calculation = Calculation(x, y, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(x,y):
        calculation = Calculation(x, y, subtract)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (x,y):
        calculation = Calculation(x, y, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(x,y):
        calculation = Calculation(x, y, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()