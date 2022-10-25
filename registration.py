import requests
# import nmap
import scapy.all as scapy
from time import sleep
import os
import json


# def get_open_ports(ip):
#     result = {}
#     scan = nmap.PortScanner().scan(hosts=ip, arguments='-sT')
#     try:
#         tcp_ports = scan.get('scan')[ip]['tcp']
#         for port, extra in tcp_ports.items():
#             result[port] = extra['name']
#     except Exception:
#         pass
#     return result

def get_vendor(mac):
    url = "https://api.macvendors.com/" + mac
    response = requests.get(url)
    if response.status_code != 200:
        print("Cannot find mac:", mac, "status code:", response.status_code)
        return "unknown device"
    return response.content.decode()


def scan(ip="192.168.50.0/24"):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
    answers = scapy.srp(arp_request, timeout=2, retry=1)[0]
    devices = []
    for _, received in answers:
        devices.append({"IP": received.psrc, 'MAC': received.hwsrc, "vendor": get_vendor(received.hwsrc)})
        sleep(1)
    return devices


def manual_connection_select(devices):
    for idx, device in enumerate(devices):
        print(f"[{idx}] IP: {device['IP']}, MAC: {device['MAC']}, vendor: {device['vendor']}")

    while selection := input("Input index of devices to choose, or enter to end"):
        register_device(devices[selection])


def register_device(device, registered_devices_path="registered_devices.json"):
    # try to create a socket connection

    # save to registered devices
    with open(registered_devices_path, 'r') as f:
        registered_devices = json.load(f)
    with open(registered_devices_path, 'w') as f:
        json.dump()
    print(device)
