from socket import *  
import os

class Server:


	def __init__(self):
		#server类的构造函数
		#创建udp套接字
		self.s = socket(AF_INET,SOCK_DGRAM)  
		self.s.bind(("127.0.0.1",9999)) 


	#找到客户端请求的文件
	def searchFile(self,targetfile):
		for parent,dirnames,filenames in os.walk("./files"):
			for filename in filenames:
				if targetfile==filename:
					return filename
			return ""

	#把文件发送给客户端
	def sendFile(self,filename,dest):
		filename="./files/"+filename
		f=open(filename,"rb")
		content=f.read(20)
		while content:
			self.s.sendto(content,dest)
			print("正在传输",content)
			content=f.read(20)
		self.s.sendto("".encode("utf-8"),dest)
		f.close()



print ('...waiting for client..')
#服务器端
#监听客户端的下载请求
server=Server()
while True:
	data= server.s.recvfrom(1024)
	if data[0].decode("utf-8").split(" ")[0]=="download":
		targetfile=data[0].decode('utf-8').split(" ")[1]
		print("客户请求下载文件：",targetfile)

		#检查服务器是否存在该文件
		filename=server.searchFile(targetfile)
		if(filename!=""):
			#开始发送文件
			print("客户请求的文件存在，开始发送")
			server.s.sendto(filename.encode("utf-8"),data[1])

			server.sendFile(filename,data[1])
		else:
			server.s.sendto("error".encode("utf-8"),data[1])
		#给客户端发送该文件


	print ("收到[%s]的请求%s"%(str(data[1]),data[0].decode('utf-8')))
	server.s.sendto("你好".encode("utf-8"),data[1])
