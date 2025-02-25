from commands.base import Command

class Invoker:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, *args):
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            raise ValueError(f"Command '{name}' not found.")
