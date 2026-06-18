def save_report(filename, target, target_ip, open_ports, common_ports):

    with open(filename, "w") as file:

        file.write(f"Target: {target}\n")

        file.write(f"IP: {target_ip}\n\n")

        for port in open_ports:

            service = common_ports.get(port, "Unknown Service")

            file.write(f"Port {port} ({service})\n")
