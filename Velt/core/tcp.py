import socket
import struct


class TCP:
    def __init__(self, s: socket.socket) -> None:
        self.socket = s

    def send(self, data: bytes) -> None:
        # Prefix each message with a 4-byte length (network byte order)
        data = struct.pack(">I", len(data)) + data
        self.socket.sendall(data)
