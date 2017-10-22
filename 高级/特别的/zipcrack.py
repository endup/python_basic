import threading
import time
import zipfile

class ZipCracker(threading.Thread):

	cracker_list=[]

	def __init__(self,target_file,index,dic):
		threading.Thread.__init__(self)
		self.stop_=False
		self.z_file=zipfile.ZipFile(target_file,"r")
		self.pwd_number=0
		self.thread_index=index
		self.dic=dic

	def __stop(self):
		self.stop_=True
		print("线程!!!~~~~",self.thread_index,"终止了")

	#@staticmethod
	def Stop(self):
		for thread in ZipCracker.cracker_list:
			thread.__stop()
		print("所有线程已经终止")

	def run(self):
		print("线程~！~~~~",self.thread_index,"启动")
		index=0
		dic_lib=open(self.dic).readlines()
		while not self.stop_:
			try:
				password=dic_lib[index].strip("\n").encode()
				index+=1
				if self.__test_pwd(password):
					print("总共尝试了",self.pwd_number,"个密码")
					time2=time.time()
					sec=time2-time1
					print("一共用了",sec,"秒")
					print("效率为：",self.pwd_number/sec,"个每秒")
			except Exception as e:
				print("!!!!!!!",e,"!!!!!!")
				self.Srop()

	def __test_pwd(self,pwd):
		self.pwd_number+=1
		if self.pwd_number%10000==0:
			print("线程",self.thread_index,"已经测试了",self.pwd_number,"个密码")
		try:
			self.z_file.extractall(pwd=pwd)
			print("密码已经破解：",pwd.decode())
			print("准备关闭所有线程")
			self.Stop()
			return True
		except:
			return False
	
	@staticmethod
	def CreateCracker(target_file,dic):
		index=1
		for i in dic:
			temp_thread=ZipCracker(target_file,index,i)
			ZipCracker.cracker_list.append(temp_thread)
			temp_thread.start()
			index+=1

dic=["pass.txt"]
time1=time.time()
ZipCracker.CreateCracker("123.zip",dic)
