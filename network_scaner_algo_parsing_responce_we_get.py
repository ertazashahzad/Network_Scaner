import scapy.all as scapy


def scan(ip):

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answerd_list = scapy.srp(arp_request_broadcast, verbose=False ,timeout = 1 )[0]


    print("IP\t\t\t\t\tMAC Address\n__________________________________________")
    for element in answerd_list:

        #print(element)
        print(element[1].psrc +"\t\t" + element[1].hwsrc)



scan("192.168.107.1/24")
