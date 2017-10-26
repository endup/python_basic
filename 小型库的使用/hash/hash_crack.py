import hashlib
import time

def createHash():
	for i in range(10000000):
		md5 = hashlib.md5()
		md5.update(str(i).encode('utf-8'))
		yield (md5.hexdigest(),i)

def checkHash(hash,cHash):
	if(hash==cHash[0]):
		print("找到密码：",cHash[1])
		return 1
	else:
		return 0

def main():
	hash=input("请输入要破解的md5密文\n")
	md5s = hashlib.md5()
	md5s.update(hash.encode('utf-8'))
	print("开始破解")
	time1=time.time()
	for cHash in createHash():
		if(checkHash(md5s.hexdigest(),cHash)):
			print("密文及其对应的密码：",cHash[0],cHash[1])
			time2=time.time()
			print("穷举了：",cHash[1]+1,"个密码\n共花费时间：",time2-time1,"\n平均速率：",(cHash[1]+1)/(time2-time1),"秒")
			break
main()
