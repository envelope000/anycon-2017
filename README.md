# anycon-2017
<h>ANYCon 2017</h1>

<b><h2>DIY Spy - Covert Channels with Scapy & Python</h2><b>

<b>Talk Code Samples</b>

  <i>(Baselining Traffic)</i>
  <b>checknet.py</b> - Usage: checknet.py <# packets to sniff>
  Will capture packets using the Sacpy sniff() function, count the layers of captured packets, and print a sorted list by frequency.
  
  <i>(Basic Data Exfiltration via Custom Layer)</i>
  <b>exfil.py</b> - To be updated
  Will send contents of a file in increments via SSDP packet contents, encoding file data in Base64 and adding to SSDP payload.
  
  <i>(Basic CNC implementation)</i>
  <b>cmd.py</b> - To be updated
  For "Bob" host: Will establish a beacon to Eve CNC via DNS, wait for a DNS-encoded command, and shell out to system. Results are sent back to Eve via an encoded HTTP request in increments.
  
  <b>rcv.py</b> - To be updated
  For "Eve" host: Will listen for beacons, pull Bob IP from DNS beacon, send commands from a file to Bob via DNS answers, and listen on port 80 for HTTP GET requests containing the encoded stdout results of the commands.

<h2>ANYCon HHV</h2>

<h3>ESP8266 & MicroPython - Covert IoT FTW!</h3>

  <b>esptool:</b> git clone https://github.com/espressif/esptool/
  <b>MicroPython:</b> Latest at http://micropython.org/download#esp8266
  <b>MP Tutorial:</b> http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html
  
  <b>main.py, boot.py</b> - load onto ESP8266 via WebREPL for exfil platform
  
