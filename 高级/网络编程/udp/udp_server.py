from socket import *  
   
s = socket(AF_INET,SOCK_DGRAM)  

s.bind(("",9999)) 
print ('...waiting for message..')
while True:
	data= s.recvfrom(1024)
	print ("[%s]:%s"%(str(data[1]),data[0].decode('utf-8')))
