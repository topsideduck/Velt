import socket

from Velt.core.tcp import TCP


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = socket.gethostbyname(host)
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

        self.clients = {}
