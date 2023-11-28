# DNS Query Tool
A simple DNS query tool implemented in Python using Tkinter for the graphical user interface. This tool allows users to perform DNS queries, IP lookups, and NS (Name Server) lookups.

## Features
DNS Query: Enter a domain and select the record type (A, AAAA, MX, CNAME, TXT) to query DNS records.
IP Lookup: Retrieve the IPv4 address of the given domain.
NS Lookup: Find the authoritative name server for the domain.

## Getting Started
Ensure you have Python installed on your system.
Install the required libraries by running:

'pip install tk ttkthemes dnspython'

Run the script using:
python dns_query_tool.py

## Usage
1. Enter the target domain in the "Domain" entry field.
2. Choose the desired record type from the dropdown menu.
3. Click "Query DNS" to perform the DNS query.
4. Use "Clear Result" to reset the result display.
5. "IP Lookup" retrieves the IPv4 address of the domain.
6. "NS Lookup" finds the authoritative name server for the domain.

## Dependencies
tkinter: GUI package for Python.
ttkthemes: ThemedStyle for Tkinter.
dnspython: DNS toolkit for Python.

## Note
This tool is designed for educational purposes and may have limitations in handling specific DNS scenarios.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
