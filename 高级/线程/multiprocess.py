from multiprocessing import Pool
import time
import os

def test():
	print("---进程池中的进程---子进程pid=%d---父进程pid=%d--" % (os.getpid(),os.getppid()))
	for i in range(3):
		print("---子进程---%d"%i)
		time.sleep(1)

	return "子进程结束"

def test2(args):
	print("---回掉函数---进程pid=%d"% os.getpid())
	print("---回掉函数---参数为：%s"%args)

pool=Pool(3)
pool.apply_async(func=test,callback=test2)

while True:
	time.sleep(1)
	print("---主进程---pid=%d"% os.getpid())