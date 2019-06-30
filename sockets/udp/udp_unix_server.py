import socket
import os


def run_server():
    unix_socket_name = 'unix.socket'
    # AF_UNIX - use file, SOCK_DGRAM - use udp protocol
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    if os.path.exists(unix_socket_name):
        os.remove(unix_socket_name)

    # Reservation file on the local machine
    server_socket.bind(unix_socket_name)
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
