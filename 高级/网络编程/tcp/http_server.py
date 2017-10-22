import socket
from threading import Thread

def handleClient(clientSocket):
	#处理连接请求
	requestData=clientSocket.recv(1024)
	print("用户请求：",requestData)
	#响应报文的处理
	responseStartLine="HTTP/1.1 200 OK\r\n"
	responseHeaders="Server:My Server\r\n"
	responseBody="hello world"
	response=responseStartLine+responseHeaders+"\r\n"+responseBody
	print("响应数据：",response)
	#向客户端响应
	clientSocket.send(bytes(response,"utf-8"))
	clientSocket.close()


def main():
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	serverAddr=("",8080)

	serverSocket.bind(serverAddr)
	serverSocket.listen(128)

	while True:
		clientSocket,clientAddr=serverSocket.accept()
		print("[%s,%s]用户连接上了" % clientAddr)
		t1=Thread(target=handleClient,args=(clientSocket,))
		t1.start()

if __name__=="__main__":
	main()