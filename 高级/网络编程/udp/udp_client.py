from socket import *  
  
s = socket(AF_INET,SOCK_DGRAM)  
#s.bind(("",8585))

while True:
	message =input('send message:>>') 
	s.sendto(message.encode("utf-8"),("127.0.0.1",9999))
