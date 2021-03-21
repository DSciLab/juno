  
import socket


def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    _, port = s.getsockname()
    s.close()
    return port


def get_hostname():
    return socket.gethostname()


if __name__ == '__main__':
    print(get_free_port())
    print(get_hostname())
