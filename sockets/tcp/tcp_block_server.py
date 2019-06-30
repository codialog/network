import socket


def run_server():
    # AF_INET - use IP4, SOCK_STREAM - use tsp protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Reservation port on the local machine
    server_socket.bind(('127.0.0.1', 8888))
    # Connection limit = 5
    server_socket.listen(5)
    # Set block on server socket and wait client
    server_socket.setblocking(True)
    # Receive 1024 bytes
    bytes_size = 1024
    # Client - client socket
    # Addr - ip address, port
    # Accept - waiting clients or take from queue
    client, addr = server_socket.accept()
    server_socket.close()
    result = client.recv(bytes_size)
    client.close()
    print('Result:', result.decode('UTF-8'))


if __name__ == '__main__':
    run_server()
