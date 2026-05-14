import socket

print("==== SIMPLE PORT SCANNER ====")

target = input("Enter target IP or domain: ")

# Common ports
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

print(f"\nScanning target: {target}")
print("-" * 40)

for port in ports:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    scanner.close()

print("\nScan Completed.")