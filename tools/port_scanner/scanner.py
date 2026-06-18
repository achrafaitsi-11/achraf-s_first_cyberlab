import socket
import time

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

# User inputs
target = input("Enter the IP address or a domain : ")
try:
    target_ip = socket.gethostbyname(target)

except socket.gaierror:

    print("Invalid IP address or domain.")

    exit()

start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

# Input validation
if start_port < 1 or end_port > 65535:
    print("Ports must be between 1 and 65535.")
    exit()

if start_port > end_port:
    print("Start port cannot be greater than end port.")
    exit()

print(f"\nScanning {target} ({target_ip})...\n")

# Start timer
start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(0.1)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:

        open_ports.append(port)

        service = common_ports.get(port, "Unknown Service")

        print(f"[+] Port {port} ({service}) is OPEN")

    scanner.close()

# End timer
end_time = time.time()

# Final results
if len(open_ports) == 0:

    print("No open ports found.")

else:

    print(f"\nFound {len(open_ports)} open port(s).")

print(f"Scan completed in {end_time - start_time:.2f} seconds.")

# Save results to a file

filename = f"scan_results_{target}.txt"

with open(filename, "w") as file:

    file.write(f"Target: {target}\n")

    file.write(f"IP: {target_ip}\n\n")

    for port in open_ports:

        service = common_ports.get(port, "Unknown Service")

        file.write(f"Port {port} ({service})\n")

print(f"\nResults saved to {filename}")