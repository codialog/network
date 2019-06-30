import socket
import time


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(0, 10):
        time.sleep(1)
        message = 'Test message {}'.format(i)
        client_socket.sendto(bytes(message, 'UTF-8'), ('127.0.0.1', 8888))


if __name__ == '__main__':
    run_client()
