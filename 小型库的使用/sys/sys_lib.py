import sys

print("脚本的名称为:",sys.argv[0].split("\\")[-1])
if len(sys.argv)>1:
	a=""
	for arg in sys.argv[1:]:
		a=a+arg+" "
	print("参数有:",a)
else:
	print("没有参数")
#path 列表是一个由目录名构成的列表, Python 从中查找扩展模块
#print(sys.path)
#python的内建模块
#print(sys.builtin_module_names)

print("当前的运行环境：",sys.platform)

#动态加载模块
time = __import__("time")
#print (os.__file__)

print(time.time())

for i in range(3):
	#print函数内部执行的
	sys.stdout.write('Dive in')
	#print("佛如")
	
#stderr输出的东西好像要比stdout要早很多(我猜只要程序中有stderr.write就会先触发这个)
#stderr跟stdout中间如果隔着个print会发生神奇的事情
time.sleep(1)
#print("nihao")
sys.stderr.write("err")

#重定向输出,重定向stderr也是类似
print ('Dive in')
print(sys.stdout)
saveout = sys.stdout        # 先在重定向前保存stdout，这样的话之后你还可以将其设回正常
fsock = open('out.log', 'w')      # 打开一个新文件用于写入。如果文件不存在，将会被创建。如果文件存在，将被覆盖。
sys.stdout = fsock                 # 所有后续的输出都会被重定向到刚才打开的新文件上。
 
print(sys.stdout)
print('This message will be logged instead of displayed')    # 这样只会将输出结果“打印”到日志文件中；屏幕上不会看到输出
print("232")
sys.stdout = saveout   # 在我们将 stdout 搞乱之前，让我们把它设回原来的方式。    
print("正常了")
fsock.close()     # 关闭日志文件。

#会先触发异常再退出
#设置退出的时候调用的函数
def exitfunc():
	print("退出")
	while True:
		print("")
sys.exitfunc = exitfunc
sys.exit(1)