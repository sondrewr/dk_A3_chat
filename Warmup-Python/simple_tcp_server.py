# A Simple TCP server, used as a warm-up exercise for assignment A3
from socket import *


def run_server():
    # TODO - implement the logic of the server, according to the protocol.
    # Take a look at the tutorial to understand the basic blocks: creating a listening socket,
    # accepting the next client connection, sending and receiving messages and closing the connection
    print("Starting TCP server...")

    welcome_socket = socket(AF_INET, SOCK_STREAM)
    welcome_socket.bin(("",1301))
    welcome_socket.listen(1)
    print("Server ready for client connections")
    need_to_run = True
    client_id = 1
    message = ""

    while need_to_run:
        connection_socket, client_adress = welcome_socket.accept()
        print("Client #%i connected" % client_id)
        message = connection_socket.recv(1024).decode()
        print("Client #%i: " % client_id, message)
        response = eval(message)
        connection_socket.send(str(response).encode())

    welcome_socket.close()
    print("Server shutting down")


# Main entrypoint of the script
if __name__ == '__main__':
    run_server()
