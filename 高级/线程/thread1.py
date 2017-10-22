import time
import threading
from threading import Thread,Lock
"""
#自己上锁
num=0
islock=False
time1=time.time()
def test1():
	global num
	global islock
	if(islock==False):
		islock=True
		for i in range(10000000):
			num+=1
		print("test1",num)
		time2=time.time()
		print("花费时间：",time2-time1)
		islock=False
	

def test2():
	global num
	global islock
	if(islock==False):
		islock=True
		for i in range(10000000):
			num+=1
		print("test2",num)
		time3=time.time()
		print("花费时间：",time3-time1)
		islock=False

t1=Thread(target=test1)
t1.start()
t2=Thread(target=test2)
t2.start()

"""
#利用内置的锁
num=0
time1=time.time()
def test1():
	global num
	mutex.acquire()
	for i in range(10000000):
		num+=1
	print("test1",num)
	time2=time.time()
	print("花费时间：",time2-time1)
	mutex.release()

def test2():
	global num
	mutex.acquire()
	for i in range(10000000):
		num+=1
	print("test2",num)
	time3=time.time()
	print("花费时间：",time3-time1)
	mutex.release()

#直接用Thread来创建进程
#创建互斥锁，默认是不上锁的
mutex=Lock()

t1=Thread(target=test1)
t1.start()
#time.sleep(1)
t2=Thread(target=test2)
t2.start()




"""
#新建一个进程类继承thread
class MyThread(Thread):
	def run(self):
		for i in range (5):
			time.sleep(1)
			msg="进程"+self.name+":"+str(i)
			print(msg)


if __name__=='__main__':
	t=Mythread()
	t.start()
"""
	