import socket
import time
from concurrent.futures import ThreadPoolExecutor

from services import common_ports
from report import save_report


def scan_port(target_ip, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:

        scanner.settimeout(0.1)

        result = scanner.connect_ex((target_ip, port))

    if result == 0:

        service = common_ports.get(port, "Unknown Service")

        print(f"[+] Port {port} ({service}) is OPEN")

        return port

    return None


def main():

    # User inputs
    target = input("Enter the IP address or a domain : ")

    try:
        target_ip = socket.gethostbyname(target)

    except socket.gaierror:

        print("Invalid IP address or domain.")
        return

    # Port range
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Input validation
    if start_port < 1 or end_port > 65535:

        print("Ports must be between 1 and 65535.")
        return

    if start_port > end_port:

        print("Start port cannot be greater than end port.")
        return

    print(f"\nScanning {target} ({target_ip})...\n")

    # Start timer
    start_time = time.time()

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        results = executor.map(
            scan_port,
            [target_ip] * (end_port - start_port + 1),
            range(start_port, end_port + 1)
        )

        for result in results:

            if result is not None:
                open_ports.append(result)

    # End timer
    end_time = time.time()

    # Final results
    if len(open_ports) == 0:

        print("No open ports found.")

    else:

        print(f"\nFound {len(open_ports)} open port(s).")

    print(f"Scan completed in {end_time - start_time:.2f} seconds.")

    # Save results
    filename = f"scan_results_{target}.txt"

    save_report(
        filename,
        target,
        target_ip,
        open_ports,
        common_ports
    )

    print(f"\nResults saved to {filename}")


if __name__ == "__main__":
    main()