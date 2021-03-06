#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from socket import *
import thread

def tcp_test(port):
    sock = socket(AF_INEF,SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect.ex((target_ip,port))
    if result ==0:
        lock.acquire()
        print "Opend Port:",port
        lock.release()

if __name__=='__man__':
    #portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)

    lock = thread.allocate_lock()

    for port in range(start_port,end_port):
        thread.start_new_thread(tcp_test,(port,))






