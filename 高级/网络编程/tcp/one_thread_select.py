import socket
import select
import sys

def main():
	host=socket.gethostname()	#取得本机的主机名
	host_ip=socket.gethostbyname(host)	#取得主机名对应的ip地址

	port=8888

	server_addr=(host_ip,port)

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)			#新建一个套接字对象
	s.bind(server_addr)		#绑定地址族到套接字对象

	s.listen(10)

	print(type(s))

	inputs=[s,sys.stdin]

	running=True

	while True:
		#调用select函数，阻塞等待
		readable,writeable,exceptional=select.select(inputs,[],[])

		#数据抵达，循环
		for sock in readable:
			if sock==s:
				#接收到新的连接
				conn,addr=s.accept()
				#把新连接加入到select的监听
				inputs.append(conn)

			#监听到键盘输入
			elif sock==sys.stdin:
				cmd=sys.stdin.readline()
				running=False
				break

			#客户端有数据抵达
			else:
				data=sock.recv(1024)
				if data:
					sock.send(data)
				else:
					#移除对该连接的监听
					inputs.remove(sock)
					sock.close()




if __name__=="__main__":
	main()