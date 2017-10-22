from socket import *  
import os

s = socket(AF_INET,SOCK_DGRAM) 
#客户端

#接收文件
def recvfile(filename,s):
	f=open(filename,"wb")
	data= s.recvfrom(1024)
	while data[0].decode('utf-8') != "":
		f.write(data[0].decode('utf-8').encode())
		data= s.recvfrom(1024)
	f.close()


#给服务器发文件下载请求
while True:
	message =input('send message:>>')
	#udp协议直接发送
	s.sendto(message.encode("utf-8"),("127.0.0.1",9999))

	if message.split(" ")[0]=="download":
		#向服务器发送文件下载的请求
		filedata=s.recvfrom(1024)
		filename=filedata[0].decode('utf-8')

		if filename !="error":
			print("请求下载的文件存在：",filename)
			#开始进行文件传输
			recvfile(filename,s)
			print("文件下载结束")

		else:
			print("请求的文件不存在")

	data= s.recvfrom(1024)
	print ("[%s]:%s"%(str(data[1]),data[0].decode('utf-8')))
