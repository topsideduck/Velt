class EchoProcessor:
    def __init__(self, command_dictionary: dict) -> None:
        self.command_dictionary = command_dictionary

    def run(self):
        return {"command": "echo", "output": f"You said: {self.command_dictionary['text']}"}

