import socket
from datetime import datetime

print("===== ADVANCED PORT SCANNER =====")

target = input("Enter the target IP address or domain name: ")

start_port = int(input("Enter the starting port number: "))
end_port =int(input("Enter the ending port number: "))

print(f"\nScanning Target: {target}")
print(f"Scanning ports {start_port} to {end_port}...\n")

start_time = datetime.now()

print("_" * 50)

try:
    for port in range(start_port, end_port + 1):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)
        result = scanner.connect_ex((target, port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"
            print(f"[OPEN] Port {port} is OPEN ({service})")
        scanner.close()
except KeyboardInterrupt:
    print("\nScan interrupted by user.")

except socket.gaierror:
    print("\nHostname could not be resolved. Exiting.")

except socket.error:
    print("\nCouldn't connect to server. Exiting.")

end_time = datetime.now()
duration = end_time - start_time

print(f"\nScan completed in {duration}.")