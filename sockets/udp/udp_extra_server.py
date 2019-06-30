# operator WITH

import socket


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', 8888))
        while True:
            result = sock.recv(1024)
            print('Message:', result.decode('utf-8'))


if __name__ == '__main__':
    run_server()
