import socket

def scan_network(ip_range, port_range):
    open_ports = {}

    for ip in ip_range:
        open_ports[ip] = []
        for port in range(port_range[0], port_range[1] + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Timeout after 1 second
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports[ip].append(port)
            sock.close()

    return open_ports
