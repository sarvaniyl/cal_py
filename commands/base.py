class Command:
    def execute(self, *args):
        raise NotImplementedError("Each command must implement the execute method.")
