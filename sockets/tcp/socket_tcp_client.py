import socket


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))
    message = 'Test message'
    client_socket.send(bytes(message, 'UTF-8'))

    result = client_socket.recv(64)
    print('Response:', result.decode())
    client_socket.close()


if __name__ == '__main__':
    run_client()

