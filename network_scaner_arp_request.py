import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    scapy.ls(scapy.ARP())


scan("192.168.107.1/24")
