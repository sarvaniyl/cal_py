import re
from commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from invoker import Invoker
from commands.base import Command
import os
import importlib

class MenuCommand(Command):
    def __init__(self, invoker):
        self.invoker = invoker

    def execute(self):
        return "Available commands: " + ", ".join(self.invoker.commands.keys())

def parse_expression(expression):
    match = re.match(r"(\d*\.?\d+)\s*([\+\-\*/])\s*(\d*\.?\d+)", expression)
    if match:
        a, operator, b = match.groups()
        return operator, float(a), float(b)
    return None

def load_plugins(invoker):
    plugin_dir = "plugins"
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{plugin_dir}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "register"):
                module.register(invoker)

def repl():
    invoker = Invoker()
    invoker.register_command("menu", MenuCommand(invoker))
    invoker.register_command("add", AddCommand())
    invoker.register_command("subtract", SubtractCommand())
    invoker.register_command("multiply", MultiplyCommand())
    invoker.register_command("divide", DivideCommand())

    load_plugins(invoker)

    operator_map = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

    print("Welcome to the Interactive Calculator! Type 'menu' for available commands.")

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            break

        parsed = parse_expression(user_input)
        if parsed:
            operator, a, b = parsed
            command_name = operator_map.get(operator)
            args = [a, b] if command_name else None
        else:
            parts = user_input.split()
            if not parts:
                print("Error: No command entered")
                continue

            command_name = parts[0]
            try:
                args = list(map(float, parts[1:]))
            except ValueError:
                print("Error: Invalid number format")
                continue

        try:
            result = invoker.execute_command(command_name, *args)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
