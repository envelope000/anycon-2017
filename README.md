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
  <b>cmd.py</b> - Eve - send commands via DNS, and sniff HTTP responses
  
  <b>rcv.py</b> - Bob - take shell commands, run, and send stdout via HTTP GET request

<h2>ANYCon HHV</h2>

<h3>ESP8266 & MicroPython - Covert IoT FTW!</h3>

See https://github.com/envelope000/anycon-2017/tree/master/esp8266


