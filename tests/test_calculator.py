from calculator import add, subtract, multiply, divide, exponential

def test_addition(): # Testing addition
    assert add(4,4) == 8

def test_subtraction(): # Test subtraction
    assert subtract(7,1) == 6

def test_multiplication(): # test multiplication
    assert multiply(1,2) == 2

def test_division(): # test division
    assert divide(4,2) == 2

def test_exponents(): ## test exponent
    assert exponential(2,2) == 4
