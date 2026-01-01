import socket

def is_host_alive(ip):
    try:
        socket.gethostbyname(ip)
        return True
    except:
        return False
