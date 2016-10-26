#!/bin/bash

import subprocess
import ipaddress
import socket
import struct 

hosts = input("Enter IPs to Nmap scan separated by ',' : ")
string_array = []
IP_array = []

string_array = hosts.split(",")
for host in string_array:
	IP_array.append(ipaddress.ip_address(host))

def NmapPingTraceroute (IP_List):
	for IP in IP_List:
		print (IP)
		print (subprocess.call(["nmap", "-sn" , "-PO[1]" , "--traceroute" , IP])) 

print ("***Nmap Scan***")
print ("(1) = Ping / Traceroute\n")
Scan_choice = input("What type of scan would you like to perform? :  \n") 

if Scan_choice == "1":
	NmapPingTraceroute(string_array)
	print ("Have a nice day!!!!")
else:
	print ("No choice was made... ")
	