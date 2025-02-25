import pytest
from commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from faker import Faker
import random

faker = Faker()

@pytest.mark.parametrize("a, b", [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(5)])
def test_add(a, b):
    command = AddCommand()
    assert command.execute(a, b) == a + b

@pytest.mark.parametrize("a, b", [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(5)])
def test_subtract(a, b):
    command = SubtractCommand()
    assert command.execute(a, b) == a - b

@pytest.mark.parametrize("a, b", [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(5)])
def test_multiply(a, b):
    command = MultiplyCommand()
    assert command.execute(a, b) == a * b

@pytest.mark.parametrize("a, b", [(random.randint(-100, 100), random.choice([0, random.randint(-100, 100)])) for _ in range(5)])
def test_divide(a, b):
    command = DivideCommand()
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            command.execute(a, b)
    else:
        assert command.execute(a, b) == a / b
