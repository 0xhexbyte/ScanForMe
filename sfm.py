#!/usr/bin/python

import scapy.all as scapy
import argparse

def scanit(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	combined_request = broadcast/arp_request
	answered_list = scapy.srp(combined_request, timeout=1, verbose=False)[0]
	clients_list=[]	
	for element in answered_list:
		client_dict={"ip":element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def printResult(results_list):
	print("IP\t\t\tMAC Address\n--------------------------------------------")
	for client in results_list:
		print (client["ip"]+"\t\t"+client["mac"])
def getInput():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--target",dest="ip",help="Use the -t, --target flag to mention the target IP address/range.")
	options = parser.parse_args()
	return options.ip
	
ip = getInput()
clients_list = scanit(ip)
printResult(clients_list)
