import socket
from threading import Thread

def main():
	host=socket.gethostname()	#取得本机的主机名
	host_ip=socket.gethostbyname(host)	#取得主机名对应的ip地址

	port=8888

	server_addr=(host_ip,port)

	server=socket.socket()			#新建一个套接字对象
	server.bind(server_addr)		#绑定地址族到套接字对象

	#设置不堵塞
	server.setblocking(False)

	server.listen(5)#监听用户的连接

	clientList=[]

	print("开始监听用户是否连接")

	while True:
		try:
			client,addr=server.accept()#接收用户的请求
		except:
			pass
		else:
			print("客户端",addr,"连接成功")
			client.setblocking(False)
			clientList.append((client,addr))

		for client,addr in clientList:
			try:
				data=client.recv(1024).decode()
			except:
				pass
			else:
				if data=="quit":
					client.close()
					clientList.remove((client,addr))
					print(addr,"连接断开")
				else:
					print(str(addr),"<<<<",data)



if __name__=="__main__":
	main()