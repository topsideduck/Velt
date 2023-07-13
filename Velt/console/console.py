from Velt.core.server import Server


class Console:
    def __init__(self) -> None:
        self.server_list: dict[str, Server] = {}
        self.current_server: Server | None = None

    def create_server(self, args):
        self.server_list[args.name] = Server(args.ip, args.port)
        return f"Create server {args.name} successfully!"



