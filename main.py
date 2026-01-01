from discovery import is_host_alive
from scanner import scan_ports
from service_enum import grab_banner
from analysis import analyze
from utils import Color
from report import generate_report


def show_banner():
    print(Color.CYAN + Color.BOLD)
    print(" ███╗   ██╗███████╗████████╗███████╗██████╗ ███████╗")
    print(" ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝")
    print(" ██╔██╗ ██║█████╗     ██║   █████╗  ██████╔╝█████╗  ")
    print(" ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██╔══██╗██╔══╝  ")
    print(" ██║ ╚████║███████╗   ██║   ███████╗██║  ██║███████╗")
    print(" ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝")
    print("        Network Reconnaissance Tool")
    print(Color.RESET)


def parse_ports(port_input):
    ports = []
    for p in port_input.split(","):
        if "-" in p:
            start, end = p.split("-")
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(p))
    return ports

def main():
    show_banner()
    target = input("Enter target IP: ")
    port_input = input("Enter ports (e.g. 22,80,443 or 1-1000): ")

    ports = parse_ports(port_input)

    if not is_host_alive(target):
        print("Host seems unreachable")
        return

    open_ports = scan_ports(target, ports)

    results = []
    for port in open_ports:
        banner = grab_banner(target, port)
        risk = analyze(port)
        results.append({"port": port, "banner": banner, "risk": risk})

    generate_report(target, results)

if __name__ == "__main__":
    main()
