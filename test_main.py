# test_main.py
import pytest
from main import Calculator

@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("input_a, input_b, expected_output", [
    (5, 3, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(calc, input_a, input_b, expected_output):
    assert calc.add(input_a, input_b) == expected_output

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply(calc):
    assert calc.multiply(5, 3) == 15
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide(calc):
    assert calc.divide(8, 2) == 4
    assert calc.divide(9, 3) == 3
    assert calc.divide(-9, 3) == -3
    assert calc.divide(-9, -3) == 3
    assert calc.divide(9, 0) == "Division by zero is not allowed!"

def test_modulus(calc):
    assert calc.modulus(9, 4) == 1
    assert calc.modulus(9, 0) == "Modulus by zero is not allowed!"

def test_factorial(calc):
    assert calc.factorial(5) == 120
    assert calc.factorial(0) == 1
    assert calc.factorial(-1) == "Factorial of negative numbers is not allowed!"