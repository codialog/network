import socket


def run_server():
    # AF_INET - use IP4, SOCK_DGRAM - use udp protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Reservation port on the local machine
    server_socket.bind(('127.0.0.1', 8888))
    # Receive 1024 bytes
    bytes_size = 1024
    while True:
        try:
            result = server_socket.recv(bytes_size)
        except KeyboardInterrupt:
            server_socket.close()
            break
        else:
            print('Result:', result.decode('UTF-8'))


if __name__ == '__main__':
    run_server()
