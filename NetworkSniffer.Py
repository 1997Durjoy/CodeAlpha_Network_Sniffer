from scapy.all import sniff
def packet_callback(packet):
    #print packet details
    print (packet.summary())

#sniff packet on the network
sniff(prn=packet_callback,count=10)  