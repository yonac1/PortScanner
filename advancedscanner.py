#!/usr/bin/env python

from socket import *
import optparse
from threading import *

sock = socket(AF_INET, SOCK_STREAM)
def connScan(tgtHost, tgtPort):
	#check if port is open
	location = (tgtHost,tgtPort)
	if sock.connect_ex(location) == 0:
                print "[X] Port %d is opened in %s" % (tgtPort, tgtHost)
     


def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost) 	
	except:
		print('Result: Unknown Host %s ' %tgtHost)
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('[+] Scan Results for: %s ' %tgtName[0])
	except:
		print('[+] Scan Results for: %s ' %tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t= Thread(target = connScan, args=(tgtHost,int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('The Usage Of The Program: \n' + '-H <target host IP/DNS> \n-r <range of ports(X-X)> \n-p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports (seperated by comma (,))')
	parser.add_option('-r', dest='tgtRangePorts', type='string', help='specify range of target ports like this: (X-X) *max range is 0 - 65534')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	tgtRange = str(options.tgtRangePorts).split('-')
	print('tgt: range %s  ' %tgtRange)
        if(tgtHost == None) | (tgtHost[0] == None):
               print(parser.usage)
               exit(0)
        if(tgtRange == None) | (tgtRange[0] ==  None) | (tgtRange[1] == None):
	        if tgtPorts[0] == None:
                        print(parser.usage)
                        exit(0)
        else: 
                start = int(tgtRange[0])
                end = int(tgtRange[1])
                if(start < 0 or end > 65534):
                        print(parser.usage)
                        exit(0)    
                for start in range(end + 1):
                        if tgtPorts[0] != None:
                                if not str(start) in tgtPorts:
                                        tgtPorts.append(str(start))
	portScan(tgtHost, tgtPorts)

if (__name__ == '__main__'):
	main()
