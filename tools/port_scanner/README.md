# Port Scanner

A small Python TCP port scanner built as part of the CyberLab project.

The tool takes an IP address or domain name, scans a user-defined range of TCP ports, identifies some common services, and saves the results to a text file.

## What it does

- Resolves domain names to IP addresses
- Scans a custom TCP port range
- Uses multiple threads to speed up scanning
- Identifies common services from their port numbers
- Displays open ports while scanning
- Saves the results to a text file

## Project structure

```text
port_scanner/
├── scanner.py
├── services.py
├── report.py
└── README.md
