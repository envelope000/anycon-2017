#!/usr/bin/python

import os, socket
from scapy.all import *
from collections import OrderedDict

i = 0
layers = []
counts = {}

packets = sniff(count=int(sys.argv[1]))
for pkt in packets:
	i=0
	while True:
		layer = pkt.getlayer(i)
		if (layer != None):
			if (layer.name not in counts):
				counts[layer.name]=0
			counts[layer.name] += 1
		else:
			break
		i += 1

sortedcounts = OrderedDict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

for prot in sortedcounts:
	if (prot != None):
		print prot, sortedcounts[prot]
