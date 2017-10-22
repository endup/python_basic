#基本思路是往exe文件中添加一点东西让系统无法再识别该exe文件

f=open("001.exe","rb")
content=f.read()
length=1/2*len(content)
f.close()

f=open("001.exe","wb")
f.seek(int(length))
f.write("hellok jkldajf".encode())
f.close()