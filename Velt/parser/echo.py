class EchoParser:
    def __init__(self, args) -> None:
        self.command_dictionary = {"command": "echo", "text": ' '.join(args.text)}

    def parse(self):
        return self.command_dictionary
