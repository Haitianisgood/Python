#-*- coding: utf-8 -*-
import SocketServer
class myTCPHandler(SocketServer.BaseRequestHandler):
    """docstring for myTCPHandler"""
    def handle(self):
        self.data = self.request.recv(4096)
        print self.data
        format_data = '\033[032.1m%a \033[0m'% self.data
        self.request.sendall(format_data.upper())


host,port = '',9999
server =  SocketServer.ThreadingTCPServer((host,port).myTCPHandler)
server.serve_forever()

