import subprocess
import scapy.all as scapy

def getting_ip_and_mac(ip):

    mac_address = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    ip_address = scapy.ARP(pdst = ip)

    ip_and_mac_combines_result = mac_address/ip_address
    final_result = scapy.srp(ip_and_mac_combines_result, timeout = 1 , verbose = False)[0]

    val = 0
    data_list = []
    for element in final_result:

        data_dic = {"index" :val, "ip" : element[1].psrc , "mac" : element[0].hwsrc}
        data_list.append(data_dic)
        #print(str(val) + "\t\t" + element[1].psrc + "\t\t" + element[1].hwsrc)
        val = val + 1
    return data_list



def print_result(final_data):
    print("Key" + "\t\t"+"IP\t\t\t\t\tMAC Address\n__________________________________________")
    for element in final_data:
        print(element["index"] , "\t\t" + element["ip"] + "\t\t" + element["mac"])


subprocess.call("ifconfig")
ip_address = input("\n\nType your ip address range : ")
final_data = getting_ip_and_mac(ip_address)
print_result(final_data)


