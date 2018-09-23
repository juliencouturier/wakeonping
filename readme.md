# Wake On Ping 
Wake on ping send a wake on lan to the specified mac address  when the specified ip address does not respond to ping.

## Requirements
The only requierments is :
* wakeonlan
`pip install -r requirements.txt`

## Run
The script takes 2 arguments : 
* The IP address to ping
* The Mac address to wake up if the ping fail