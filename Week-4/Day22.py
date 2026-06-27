# VS Code debugger: breakpoints, F10, F11
# Watch variables in real time
# pip install pytest
# def test_add(): assert add(2,3) == 5
# Run: pytest test_calculator.py
# Analogy: Debugging = oscilloscope. Pytest = inspection gauge.



# Day22.py — Week 4 Saturday: Testing & Debugging
# VS Code debugger: breakpoints, F10, F11
# Watch variables in real time
# pip install pytest
# Analogy: Debugging = oscilloscope. Pytest = inspection gauge.

import pytest
from cal import add, subtract, multiply, divide
from Day21 import format_quote


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_format_quote():
    result = format_quote("Life is short", "Buddha")
    assert result == "Life is short — Buddha"
        
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
    