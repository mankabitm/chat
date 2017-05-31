#!/usr/bin/python
import socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("192.168.1.100",3000))

while 3<4:
	recieve = ""
	recieve = (x.recvfrom(1000))[0]
	#ip = recieve[1][0]
	#port =int(recieve[1][1])
	print "sender::   "+recieve
	
	reply = raw_input("you::  ")
	x.sendto(reply,("192.168.1.10",2000))
	
	
		
		
