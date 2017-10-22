import socket
import configparser

class portMaker:
	def __init__(self,portFilePath):
		#创建config对象
		self.config=configparser.ConfigParser()
		self.config.readfp(open(portFilePath))
		#初始化端口列表
		self.portList=[]
		self.initializePort()
		#存储有效的端口
		self.workedList=[]

	def initializePort(self):
		'''
		portNumber=int(self.config.get("PORT","portNumber"))
		for i in range(portNumber):
			portOption="port"+str(i)
			self.portList.append(int(self.config.get("PORT",portOption)))
			'''
		for i in range(1000):
			#portOption="port"+str(i)
			self.portList.append(i)
			

def testConnect(port,ip,wrokList):
	serverAddr=(ip,port)
	client=socket.socket()
	print("尝试连接服务器",serverAddr)

	try:
		client.settimeout(.1)
		print(serverAddr)
		client.connect(serverAddr)
		message=client.recv(1024).decode()
		print("连接成功!!!")
		print(message)
		workList.append(port)
	except:
		print("连接失败~~~")

url="www.baidu.com"
porter=portMaker("ports.ini")
ip=socket.gethostbyname(url)

for i in porter.portList:
	testConnect(i,ip,porter.workedList)

print("worked port like above...")
for i in porter.workedList:
	print(i)