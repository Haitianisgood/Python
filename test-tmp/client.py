#-*- coding: utf-8 -*-
import socket
HOST = '10.0.0.34'
PORT = 5007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
#s.sendall('Hello,world')
while 1:
    INPUT = raw_input("input:")
    s.send(INPUT)
    data = s.recv(1024)
    print 'Result:',data
s.close()
#print 'Received',repr(data)
