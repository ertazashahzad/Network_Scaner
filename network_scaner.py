#!/usr/bin/env python

import scapy.all as scapy
import subprocess
import os
import re

subprocess.call(["ifconfig"])


def chose_interface():
    interface = input("Chose Interface : ")
    os.system("clear")
    subprocess.call(["ifconfig", interface])
    interface_result = subprocess.check_output(["ifconfig", interface])
    interface_result = interface_result.decode("utf-8")
    return interface_result


def get_ip_address(interface_result):
    search_result = re.search(r".inet \d\d\d.\d\d\d.\d\d\d.\d\d\d", interface_result)
    print("Your IP Address is : ",str(search_result.group(0)))


def scaner():
    ip = input("Write Your IP Address Range To show Devices : ")
    scapy.arping(str(ip))



interface_result = chose_interface()
get_ip_address(interface_result)
scaner()

#IP Value
#192.168.107.1/24