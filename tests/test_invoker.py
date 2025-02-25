import pytest
from invoker import Invoker
from commands.basic import AddCommand

def test_execute_registered_command():
    invoker = Invoker()
    invoker.register_command("add", AddCommand())

    result = invoker.execute_command("add", 3, 2)
    assert result == 5

def test_execute_unregistered_command():
    invoker = Invoker()

    with pytest.raises(ValueError):
        invoker.execute_command("subtract", 3, 2)
