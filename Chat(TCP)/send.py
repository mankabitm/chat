#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.100",9999))
while 4>3:
	r=raw_input("Enter your message:")
	s.send(r)
	print s.recv(100)
s.close()
