<h1>ANYCon 2017</h1>

<b><h2>DIY Spy - Covert Channels with Scapy & Python</h2></b>

<b>Talk Code Samples</b>

  <i>(Baselining Traffic)</i><br>
  <b>checknet.py</b> - Usage: checknet.py <# packets to sniff><br>
  Will capture packets using the Sacpy sniff() function, count the layers of captured packets, and print a sorted list by frequency.
  
  <i>(Basic Data Exfiltration via Custom Layer)</i><br>
  <b>exfil.py</b> - To be updated<br>
  Will send contents of a file in increments via SSDP packet contents, encoding file data in Base64 and adding to SSDP payload.
  
  <i>(Basic CNC implementation)</i><br>
  <b>cmd.py</b> - To be updated<br>
  For "Bob" host: Will establish a beacon to Eve CNC via DNS, wait for a DNS-encoded command, and shell out to system. Results are sent back to Eve via an encoded HTTP request in increments.
  
  <b>rcv.py</b> - To be updated<br>
  For "Eve" host: Will listen for beacons, pull Bob IP from DNS beacon, send commands from a file to Bob via DNS answers, and listen on port 80 for HTTP GET requests containing the encoded stdout results of the commands.

<h2>ANYCon HHV</h2>

<h3>ESP8266 & MicroPython - Covert IoT FTW!</h3>

See https://github.com/envelope000/anycon-2017/esp8266


