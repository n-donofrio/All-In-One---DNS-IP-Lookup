# Code by Nicholas Donofrio
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import dns.resolver
import socket


def query_dns():
    domain = entry_domain.get()
    record_type = combo_record_type.get()

    try:
        result = dns.resolver.query(domain, record_type)
        result_text.set("\n".join(f'{record_type}: {record.to_text()}' for record in result))
        update_status("Query successful.")
    except dns.resolver.NoAnswer:
        result_text.set(f"No {record_type} records found for {domain}")
        update_status(f"No {record_type} records found.")
    except Exception as e:
        result_text.set(f"Error: {e}")
        update_status("Error during query.")


def clear_result():
    result_text.set("")
    update_status("Ready")


def ip_lookup():
    domain = entry_domain.get()

    try:
        # Get both IPv4 and IPv6 addresses
        ip_address = socket.gethostbyname(domain)

        # Clear status before updating
        clear_result()
        update_status(f"IPv4 Address: {ip_address}")
    except socket.gaierror as e:
        update_status(f"Error: {e}")


def ns_lookup():
    domain = entry_domain.get()

    try:
        # Get authoritative name server for the domain
        ns_records = dns.resolver.query(domain, 'NS')
        ns_list = [record.to_text() for record in ns_records]

        # Get the server and address for the first name server
        server_address = None
        for ns_server in ns_list:
            try:
                ns_server_ip = socket.gethostbyname(ns_server)
                server_address = f"Server: {ns_server}"
                break
            except socket.gaierror:
                continue

        # Clear status before updating
        clear_result()

        if server_address:
            update_status(server_address)
        else:
            update_status(f"No valid NS server found for {domain}")
    except dns.resolver.NoAnswer:
        update_status(f"No NS records found for {domain}")
    except Exception as e:
        update_status(f"Error: {e}")

def update_status(message):
    status_bar.config(text=message)


# GUI setup
root = tk.Tk()
root.title("DNS Query Tool")

# Use ThemedStyle to apply a Windows theme
style = ThemedStyle(root)
style.set_theme("vista")

# Set default window size
width = 1280
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - width) // 2
y_position = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x_position}+{y_position}")

# Labels
label_domain = ttk.Label(root, text="Domain:")
label_record_type = ttk.Label(root, text="Record Type:")

# Entry widgets
entry_domain = ttk.Entry(root)
entry_domain.insert(0, "www.example.com")  # Default domain
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, wraplength=350)  # Set wraplength

# Combo box for record type
record_types = ["A", "AAAA", "MX", "CNAME", "TXT"]  # Add more as needed
combo_record_type = ttk.Combobox(root, values=record_types)
combo_record_type.set("A")  # Default record type

# Query, Clear, IP Lookup, and NS Lookup buttons
btn_query = ttk.Button(root, text="Query DNS", command=query_dns, width=15)  # Set width
btn_clear = ttk.Button(root, text="Clear Result", command=clear_result, width=15)  # Set width
ip_lookup_button = ttk.Button(root, text="IP Lookup", command=ip_lookup, width=15)  # Set width
ns_lookup_button = ttk.Button(root, text="NS Lookup", command=ns_lookup, width=15)  # Set width


# Status bar
status_bar = ttk.Label(root, text="Ready", anchor=tk.W)
status_bar.grid(row=4, column=0, columnspan=3, sticky="WE")

# Layout
label_domain.grid(row=0, column=0, sticky="E", pady=(10, 0))
label_record_type.grid(row=1, column=0, sticky="E")
entry_domain.grid(row=0, column=1, pady=(10, 0))
combo_record_type.grid(row=1, column=1)
btn_query.grid(row=2, column=1, pady=5)
btn_clear.grid(row=2, column=0, pady=5)
ip_lookup_button.grid(row=2, column=2, pady=5)  # Adjusted column position
ns_lookup_button.grid(row=2, column=3, pady=5)  # New button
result_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))


# Run the GUI
root.mainloop()
