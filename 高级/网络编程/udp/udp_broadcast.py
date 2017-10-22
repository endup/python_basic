import sys
from socket import *  

dest=('<broadcast>',7788)

s= socket(AF_INET,SOCK_DGRAM)  
#设置广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.sendto(b"HI",dest)

print("等待对方回复")

while True:
	(buf,address)=s.recvfrom(2048)
	print("Received from %s : %s" % (address,buff))

