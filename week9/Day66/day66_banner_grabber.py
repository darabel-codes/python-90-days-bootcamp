from datetime import datetime
import socket


print("===== BANNER GRABBER =====")

target = input("Enter the target IP address or domain name: ")
port = int(input("Enter the port number to grab the banner from: "))

try:
    
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    scanner.settimeout(3)
    
    scanner.connect((target, port))
    banner = scanner.recv(1024)
    
    print("\n[+] Banner Received:")
    print(banner.decode().strip())
    
    scanner.close()
    
    if not banner:
        print("\n[-] No banner received. The service may not provide a banner or the port may be closed.")
    else:
        with open("banner_notes.txt", "w") as file:
            file.write(f"Target: {target}\nPort: {port}\nBanner: {banner.decode().strip()}\n")
            print("\n[+] Banner information saved to banner_notes.txt")

    

except socket.timeout:
    print("\n[-] Connection timed out. No banner received.")

except ConnectionRefusedError:
    print("\n[-] Connection refused. The port may be closed.")

except socket.gaierror:
    print("\n[-] Hostname invalid.")

except Exception as e:
    print(f"\n[-] An error occurred: {e}")

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"\nScan completed at {time}.")