from scapy.all import sniff

print("==== SIMPLE PACKET SNIFFER ====")

def packet_callback(packet):

    print(packet.summary())

sniff(prn=packet_callback, count=10)

print("\nSniffing completed.")