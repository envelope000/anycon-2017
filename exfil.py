#!/usr/bin/python

import os
import socket
from scapy.all import *


SSDP_Raw = "M-SEARCH * HTTP/1.1\r\n" \
	"HOST:239.255.255.250:1900\r\n" \
	"ST:upnp:rootdevice\r\n" \
	"MAN: \"ssdp:discover\"\r\n" \
	"MX:2\r\n\r\n"

rawpkt = IP(dst="239.255.255.250") / UDP(sport=1900, dport= 1900) / SSDP_Raw
send(rawpkt)


class SSDP(Packet):
  fields_desc=[
        StrField("RequestMethod", 'NOTIFY'),
        StrField("space", " "),
        StrField("RequestURI","*"),
        StrField("space", " "),
        StrField("RequestVersion","HTTP/1.1")
  ]

	

classpkt=IP(dst='239.255.255.250')/UDP(sport=1900,dport=1900)/SSDP()
ls(SSDP)
send(classpkt)

