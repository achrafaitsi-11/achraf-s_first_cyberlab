# Port Scanner

A Python port scanner developed as part of my summer cybersecurity portfolio project.

The goal of this project was to move beyond basic Python exercises and build a practical cybersecurity tool while learning how to structure, document and maintain a GitHub repository.

## Features

* Scan a custom range of ports
* Detect open ports
* Identify common services
* Accept both IP addresses and domain names
* Use multithreading to improve scanning speed
* Generate a text report containing the results
* Validate user input

## Project structure

```
port_scanner/

scanner.py
services.py
report.py
README.md
```

## Requirements

* Python 3.x

## Usage

Run the program:

```bash
python scanner.py
```

Example:

```text
Enter an IP address or domain: scanme.nmap.org
Enter the start port: 20
Enter the end port: 100
```

## What I learned

This project helped me practice:

* Python networking with the socket module
* Multithreading with ThreadPoolExecutor
* Modular programming
* Git and GitHub workflow
* Project documentation

## Disclaimer

This project was created for educational purposes only.

Only scan systems that you own or have explicit permission to test.

