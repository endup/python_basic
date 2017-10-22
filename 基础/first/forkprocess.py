import os 
import time
from multiprocessing import Process

"""
#window内核中没有fork函数
res=os.fork()
#调用函数的时候会自动新建一个进程，返回值为0的为子进程，返回值>0的为父进程

if res==0:
	while True:
		print("~~~子进程~~~")
		time.sleep(1)

else:
	while True:
		print("~~~父进程~~~")
		time.sleep(1)

"""

def test():
	while True:
		print("进程")
		time.sleep(1)

p=Process(target=test)		#创建进程
p.start()					#运行进程

while True:
	print("main")
	time.sleep(1)
