from calculator.operations import add, subtract, multiply, divide
# Keeping tests similar to main branch from previous homework.

def test_addition(): # Testing addition
    '''Testing addition function'''
    assert add(4,4) == 8

def test_subtraction(): # Test subtraction
    '''Testing subtraction function'''
    assert subtract(7,1) == 6

def test_multiplication(): # test multiplication
    '''Testing multiplication function'''
    assert multiply(1,2) == 2

def test_division(): # test division
    '''Testing division function'''
    assert divide(4,2) == 2
