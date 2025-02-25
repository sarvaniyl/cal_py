import pytest
from commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_addition():
    assert AddCommand().execute(3, 2) == 5

def test_subtraction():
    assert SubtractCommand().execute(5, 3) == 2

def test_multiplication():
    assert MultiplyCommand().execute(4, 3) == 12

def test_division():
    assert DivideCommand().execute(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        DivideCommand().execute(5, 0)
