import socket
from threading import Thread


def main():
	global client
	host=socket.gethostname()	#取得本机的主机名
	host_ip=socket.gethostbyname(host)	#取得主机名对应的ip地址

	port=8888

	server_addr=(host_ip,port)

	client=socket.socket()			#新建一个套接字对象
	client.connect_ex(server_addr)		#连接对应的服务器

	print("连接服务器")
	#会等待服务端发送消息直到结束连接
	

	t1=Thread(target=send)
	t1.start()

	t2=Thread(target=receive)
	t2.start()
			

def receive():
	while 1:
		try:
			rmsg=client.recv(1024).decode()
			print("\r服务器<<<<",rmsg)
			print(">>>>")
		except:
			print("连接中断")
			break
def send():
	while 1:
		try:
			smsg=input(">>>>")
			client.send(smsg.encode())
			if(smsg=="quit"):
				client.close()
				break
		except:
			print("连接中断")
			break


if __name__=="__main__":
	main()
