from socket import *  
import os


#找到客户端请求的文件
def searchFile(targetfile):
	for parent,dirnames,filenames in os.walk("./files"):
		for filename in filenames:
			if targetfile==filename:
				return filename
		return ""


#把文件发送给客户端
def sendFile(filename,s,dest):
	filename="./files/"+filename
	f=open(filename,"rb")
	content=f.read(1010)
	while content:
		s.sendto(content,dest)
		print("正在传输",content)
		content=f.read(1010)
	s.sendto("".encode("utf-8"),dest)
	f.close()


#创建udp套接字
s = socket(AF_INET,SOCK_DGRAM)  

s.bind(("127.0.0.1",9999)) 
print ('...waiting for client..')

#rootdir="C:\\Users\s\Desktop\file"
#服务器端

#监听客户端的下载请求
while True:
	data= s.recvfrom(1024)


	if data[0].decode("utf-8").split(" ")[0]=="download":
		targetfile=data[0].decode('utf-8').split(" ")[1]
		print("客户请求下载文件：",targetfile)
		#检查服务器是否存在该文件
		filename=searchFile(targetfile)
		if(filename!=""):
			#开始发送文件
			print("客户请求的文件存在，开始发送")
			s.sendto(filename.encode("utf-8"),data[1])

			sendFile(filename,s,data[1])
		else:
			s.sendto("error".encode("utf-8"),data[1])
		#给客户端发送该文件


	print ("收到[%s]的请求%s"%(str(data[1]),data[0].decode('utf-8')))
	s.sendto("你好".encode("utf-8"),data[1])

	