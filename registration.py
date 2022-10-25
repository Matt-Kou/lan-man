import pickle
import socket

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
        devices.append(UnregisteredDevice(ip=received.psrc, mac=received.hwsrc, vendor=get_vendor(received.hwsrc)))
        sleep(1)
    return devices


class Device:
    def __init__(self, ip, mac, vendor):
        self.ip = ip
        self.mac = mac
        self.vendor = vendor
        self.hostname = None

    def __str__(self):
        s = f"IP: {self.ip}, MAC: {self.mac}, Vendor: {self.vendor}"
        if self.hostname:
            s = f"Hostname: {self.hostname}, " + s
        return s


class UnregisteredDevice(Device):
    def __init__(self, ip, mac, vendor):
        super().__init__(ip, mac, vendor)

    def register(self):
        # try to create a TCP connection
        registration_req = ("registration_req", "")  # content left blank for future usage
        PORT = 65432
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, PORT))
            s.sendall(pickle.dumps(registration_req))
            data = s.recv(4096)
            if not data:
                raise Exception("No acknowledgement response from server.")
            data_type, content = pickle.loads(data)
            if data_type != "registration_ack":
                raise Exception("Must be a registration acknowledgement.")
        print(f"connection with the device:\n{self}\n successful.")

# def manual_connection_select(devices):
#     for idx, device in enumerate(devices):
#         print(f"[{idx}] IP: {device['IP']}, MAC: {device['MAC']}, vendor: {device['vendor']}")
#
#     while selection := input("Input index of devices to choose, or enter to end"):
#         register_device(devices[selection])


# def register_device(device, registered_devices_path="registered_devices.json"):
#     # try to create a socket connection
#
#     # save to registered devices
#     with open(registered_devices_path, 'r') as f:
#         registered_devices = json.load(f)
#     with open(registered_devices_path, 'w') as f:
#         json.dump()
#     print(device)
