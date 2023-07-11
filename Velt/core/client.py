import pickle
import socket
import time

from Velt.core.tcp import TCP


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = socket.gethostbyname(host)
        self.port = port

        self.tcp = TCP(self.connect())

    def connect(self) -> socket.socket:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                print("Connected!")

                return s

            except socket.error:
                time.sleep(3)
