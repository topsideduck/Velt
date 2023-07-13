import pickle
import socket
import time

from Velt.core.tcp import TCP
from Velt.processor.echo import EchoProcessor


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = socket.gethostbyname(host)
        self.port = port

        self.tcp = TCP(self.connect())

        self.processor_mapping = {"echo": EchoProcessor}

    def connect(self) -> socket.socket:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                print("Connected!")

                return s

            except socket.error:
                time.sleep(3)

    def execute(self, command: dict):
        return self.processor_mapping[command["command"]](command).run()

    def run(self):
        while True:
            try:
                data = pickle.loads(self.tcp.receive())
                output = self.execute(data)
                self.tcp.send(pickle.dumps(output))

            except (socket.error, TypeError, BrokenPipeError):
                print("Disconnected!")
                self.tcp = TCP(self.connect())


if __name__ == '__main__':
    client = Client('localhost', 4444)
    client.run()
