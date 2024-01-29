import scapy.all as scapy


def scan(ip):

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answerd_list, unanswerd_list = scapy.srp(arp_request_broadcast, timeout = 1)

    print(answerd_list.summary())

scan("192.168.107.1/24")
