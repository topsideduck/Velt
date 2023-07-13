import argparse

create_server_parser = argparse.ArgumentParser(
    prog="create_server",
    description="Create a new server to listen to incoming connections",
    exit_on_error=False,
)
create_server_parser.add_argument(
    "name",
    type=str,
    help="The name of the server. This is for the user to identify the server.",
)
create_server_parser.add_argument("ip", type=str, help="The IP of the server.")
create_server_parser.add_argument("port", type=int, help="The port to listen to.")


echo_parser = argparse.ArgumentParser(
    prog="echo", description="Echo text back to the server.", exit_on_error=False
)
echo_parser.add_argument("text", nargs="*", type=str, help="The text to echo back.")
