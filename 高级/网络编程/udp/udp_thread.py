from socket import *  
from threading import Thread

def main():
	global s,linkport
	s= socket(AF_INET,SOCK_DGRAM)  
	port=9999
	linkport=10000
	while True:
		try:
			s.bind(("127.0.0.1",port)) 
			break
		except:
			linkport=port
			port+=1
			#print(port)
			continue


	print ('start chatting')

	t1=Thread(target=send)
	t1.start()

	t2=Thread(target=receive)
	t2.start()

def send():
	while True:
		message=input('你说:<<<<')
		if message=="":
			print("你发送的内容为空")
			continue
		s.sendto(message.encode("utf-8"),("127.0.0.1",linkport))

def receive():
	while True:
		try:
			data= s.recvfrom(1024)
			#print ("[%s]:%s"%(str(data[1]),data[0].decode('utf-8')))
			print ("\r对方说>>>>:%s"%(data[0].decode('utf-8')))
			print("你说:<<<<")
		except:
			continue

if __name__=="__main__":
	main()
