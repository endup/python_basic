import socket
from threading import Thread

def main():
	#global soc,addr
	host=socket.gethostname()	#取得本机的主机名
	host_ip=socket.gethostbyname(host)	#取得主机名对应的ip地址

	port=8888

	server_addr=(host_ip,port)

	server=socket.socket()			#新建一个套接字对象
	server.bind(server_addr)		#绑定地址族到套接字对象

	server.listen(5)#监听用户的连接
	print("开始监听用户是否连接")
	try:
		while 1:
			soc,addr=server.accept()#接收用户的请求

			t0=Thread(target=accept_,args=(soc,addr))
			t0.start()
		
	finally:
		print("关闭服务器")
		server.close()

def accept2(soc,addr):
	while True:
		rmsg=soc.recv(1024).decode()
		if(rmsg=="quit"):
			print("客户端中断连接")
			break
		print("\r客户端<<<<",rmsg)
	soc.close()



def accept_(soc,addr):
	print(addr,"用户连接")

	t1=Thread(target=send,args=(soc,addr))
	t1.start()

	t2=Thread(target=receive,args=(soc,addr))
	t2.start()

def receive(soc,addr):
	while 1:
		try:
			rmsg=soc.recv(1024).decode()
			if(rmsg=="quit"):
				print(addr,"用户中断连接")
				
				break
			print("\r客户端<<<<",rmsg)
			print(">>>>")
		except:
			print("连接中断")
			break
	soc.close()

def send(soc,addr):
	while 1:
		try:
			smsg=input(">>>>")
			soc.send(smsg.encode())
		except:
			print("连接中断")
			break


if __name__=="__main__":
	main()