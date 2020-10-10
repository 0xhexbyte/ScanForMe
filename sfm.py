#!/usr/bin/python

import scapy.all as scapy

def scanit(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	combined_request = broadcast/arp_request
	(answered_list, unanswered_list) = scapy.srp(combined_request, timeout=1, verbose=False)
	print("IP\t\t\tMAC Address\n--------------------------------------------")
	for element in answered_list:
		print(element[1].psrc + "\t\t" +element[1].hwsrc)

scanit("Enter IP here")
