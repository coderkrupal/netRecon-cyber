from utils import tcp_connect
 

def grab_banner(ip, port):
    try:
        sock = tcp_connect(ip, port)
        if not sock:
            return None

        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return banner.strip()
    except:
        return None
