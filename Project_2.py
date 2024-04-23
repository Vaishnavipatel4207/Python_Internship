
#Project Title: Port Scanner in Python

import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()

    except Exception as e:
        print(f"Error while scanning port {port}: {e}")


def scan_range(host, start_port, end_port):
    print(f"Scanning ports on {host}...")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)
    print("Scan completed.")    

if __name__ == "__main__":
    target_host = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scan_range(target_host, start_port, end_port)







