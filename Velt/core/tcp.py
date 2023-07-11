import socket
import struct


class TCP:
    def __init__(self, s: socket.socket) -> None:
        self.socket = s

    def send(self, data: bytes) -> None:
        # Prefix each message with a 4-byte length (network byte order)
        data = struct.pack(">I", len(data)) + data
        self.socket.sendall(data)

    def receive(self) -> bytearray | None:
        # Read message length and unpack it into an integer
        raw_data_length = self._receive_all(4)

        if not raw_data_length:
            return None

        data_length = struct.unpack(">I", raw_data_length)[0]

        # Read the message data
        return self._receive_all(data_length)

    def _receive_all(self, n: int) -> bytearray | None:
        # Helper function to recv n bytes or return None if EOF is hit
        data = bytearray()

        while len(data) < n:
            packet = self.socket.recv(n - len(data))
            if not packet:
                return None

            data.extend(packet)

        return data
