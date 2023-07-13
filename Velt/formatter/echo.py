class EchoFormatter:
    def __init__(self, result_dictionary: dict) -> None:
        self.result_dictionary = result_dictionary

    def format_output(self):
        return self.result_dictionary["output"]
