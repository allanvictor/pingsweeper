# PING SWEEPPER
Scan ips and show lives and deads in Network
## Dependencies:
- python 3.x.x
- scapy
- netaddr
### Installing Depedencies:
```
pip install -r requirements.txt
```
## Usage
### Default Usage (Show lives and deads):
put command plus ip/cidr example:
```
python pingsweeper.py 192.168.0.0/24
```
### Show only lives:
```
python pingsweeper.py -l 192.168.0.0/24
```
### Show only deads: 
```
python pingsweeper.py -d 192.168.0.0/24
```