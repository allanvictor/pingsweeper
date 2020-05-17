#!/usr/bin/python
import  logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *
from netaddr import *
import socket
import sys, getopt

def getlive():
    for i in live:
        print('live {0}'.format(i[0].dst))
def getdead():
    for j in dead:
        print('dead {0}'.format(j[0].dst))
def usage():
    print('Usage: pingsweeper [options] <ip>\n\t-l show live hosts\n\t-d show dead hosts\n\n--Development By Allan Victor--')
    exit()
if(len(sys.argv)>1):
    opts, args = getopt.getopt(sys.argv[1:],'ldh')
    try:
        target=args[0]
    except:
        usage()
    try:
        ip_range=IPNetwork(target)
        for ip in ip_range:
            if str(ip_range.cidr) != str(ip)+'/32':
                if ip == ip_range.network or ip == ip_range.broadcast:
                    continue
            live,dead=sr(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
            if not opts:
                getlive()
                getdead()
            else:
                for opt in opts:
                    if ('-l' in opt):
                        getlive()
                    elif ('-d' in opt):
                        getdead()
                    elif ('h' in opt):
                        usage()
    except:
        logging.getLogger(__name__).warning('ERROR:Illegal IP')
        usage()
else:
    usage()
