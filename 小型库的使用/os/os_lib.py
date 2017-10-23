import os
#获取目录
print(os.getcwd())
#获取目录下的文件
print(os.listdir())
#删除文件
#os.remove("out.log")
print(os.listdir())
#调用命令行
#os.system("ping www.baidu.com")
#切换目录
os.chdir("../")
print("当前系统路径分隔符：",os.sep)
print(os.getcwd())
#获取环境变量
print(os.getenv('PATH'))

#获取并修改环境变量
print(type(os.environ['PATH']))
os.environ['PATH']+=";aaaaaa"
print("",os.environ["PATH"])

size=os.path.getsize("C:/Users/s/Desktop/python-3.7.0a1-amd64.exe")
print(size/1024,"kb")