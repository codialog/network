import socket


def run_server():
    # AF_INET - use IP4, SOCK_STREAM - use tsp protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Reservation port on the local machine
    server_socket.bind(('127.0.0.1', 8888))
    # Connection limit = 5
    server_socket.listen(5)
    # wait client 5 seconds, after setblocking(False) it's row 14
    server_socket.settimeout(5)
    # Unset block on server socket and wait client
    # server_socket.setblocking(False)
    # Receive 1024 bytes
    bytes_size = 1024
    while True:
        try:
            # Client - client socket
            # Addr - ip address, port
            # Accept - waiting clients or take from queue
            client, addr = server_socket.accept()
        except socket.error:
            print('no clients')
        except KeyboardInterrupt:
            break
        else:
            client.setblocking(True)
            result = client.recv(bytes_size)
            client.close()
            print('Result:', result.decode('UTF-8'))


if __name__ == '__main__':
    run_server()
