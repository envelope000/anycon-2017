# anycon-2017
ANYCon 2017

DIY Spy - Covert Channels with Scapy & Python

Talk Code Samples

  (Baselining Traffic)
  checknet.py - Usage: checknet.py <# packets to sniff>
  Will capture packets using the Sacpy sniff() function, count the layers of captured packets, and print a sorted list by frequency.
  
  (Basic Data Exfiltration via Custom Layer)
  exfil.py - To be updated
  Will send contents of a file in increments via SSDP packet contents, encoding file data in Base64 and adding to SSDP payload.
  
  
  (Basic CNC implementation)
  
  cmd.py - To be updated
  For "Bob" host: Will establish a beacon to Eve CNC via DNS, wait for a DNS-encoded command, and shell out to system. Results are sent back to Eve via an encoded HTTP request in increments.
  
  rcv.py - To be updated
  For "Eve" host: Will listen for beacons, pull Bob IP from DNS beacon, send commands from a file to Bob via DNS answers, and listen on port 80 for HTTP GET requests containing the encoded stdout results of the commands.

ANYCon HHV

ESP8266 & MicroPython - Covert IoT FTW!

  esptool: git clone https://github.com/espressif/esptool/
  MicroPython: Latest at http://micropython.org/download#esp8266
  MP Tutorial: http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html
  
  main.py, boot.py - load onto ESP8266 via WebREPL for exfil platform
  
