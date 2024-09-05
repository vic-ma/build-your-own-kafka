import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 9092), reuse_port=True)
    server_socket.accept() # wait for client


if __name__ == "__main__":
    main()