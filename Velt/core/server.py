import socket

from threading import Thread

from Velt.core.tcp import TCP


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = socket.gethostbyname(host)
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

        self.clients = {}

        self.connection_thread = Thread(
            target=self.accept_incoming_collections,
            name="Accept incoming connections",
            daemon=True,
        )
        self.connection_thread.start()

        self.client: str | None = None

    def accept_incoming_collections(self) -> None:
        self.server_socket.listen(0)

        while True:
            client_socket, client_address = self.server_socket.accept()
            client_name = ":".join([str(i) for i in client_address])
            print(f"Accepted connection from {client_name}!")

            client_data = {
                "ip": client_address[0],
                "port": client_address[1],
                "socket": client_socket,
                "tcp": TCP(client_socket),
            }

            self.clients[client_name] = client_data

