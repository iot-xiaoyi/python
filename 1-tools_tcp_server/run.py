# -*- coding: utf8 -*-
import os
import socketserver

########## tcp server 
class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            print ("##################receive from (%r):%r" % (self.client_address, data))
            self.request.send( data )
            
host = ("192.168.1.7", 8089)
tcp_s = socketserver.ThreadingTCPServer(host, MyTcpServer)
tcp_s.serve_forever()