import pickle
import socket
import time

from Velt.core.tcp import TCP


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = socket.gethostbyname(host)
        self.port = port
