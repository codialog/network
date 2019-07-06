import socket

from http.parse_http_response import parse_http_response

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('example.com', 80))
    content_items = [
        'GET / HTTP/1.1',
        'Host: example.com',
        'Connection: keep-alive',
        'Accept: text/html',
        '\n'
    ]
    content = '\n'.join(content_items)
    print('---HTTP MESSAGE---')
    print(content)
    print('---END OF MESSAGE---')
    sock.send(content.encode())
    result = sock.recv(10024)
    status_code, headers, content = parse_http_response(result.decode())
    print('Status code: {}'.format(status_code))
    print('Headers: {}'.format(headers))
    print('Content: {}'.format(content))
