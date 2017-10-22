from socket import *
import struct

data=struct.pack("!H8sb5sb",1,b"test.jpg",0,b"octet",0)

#s=socket(AF_INET,SOCK_DGRAM)
#s.sendto(data,("127.0.0.1",9999))

result=struct.unpack("!8s",data[2:10])

print(data)
print(result)

#s.close()