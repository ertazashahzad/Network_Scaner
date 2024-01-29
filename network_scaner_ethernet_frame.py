import scapy.all as scapy


def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)

    arp_request.show()
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    broadcast.show()
    print(broadcast.summary())
    # scapy.ls(scapy.Ether())

    arp_request_broadcast = broadcast/arp_request

    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


scan("192.168.107.1/24")
