#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",9999))
s.listen(5)
while 4>3:
	cliport,cliaddr=s.accept()
	print cliport.recv(100)
	#print "From client ip->",cliaddr
	r=raw_input("Enter your reply:")
	cliport.send(r)
s.close()
