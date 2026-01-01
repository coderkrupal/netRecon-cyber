from utils import tcp_connect

def scan_ports(ip, ports):
    open_ports = []

    for port in ports:
        sock = tcp_connect(ip, port)
        if sock:
            open_ports.append(port)
            sock.close()

    return open_ports
