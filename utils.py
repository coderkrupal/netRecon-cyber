import socket

class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def tcp_connect(ip, port, timeout=1):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        return s
    except:
        return None
