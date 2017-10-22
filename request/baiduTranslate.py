import requests
import json

class Translate:
	def __init__(self):
		self.url="http://fanyi.baidu.com/v2transapi"
	#创建url后面的请求参数
	def mkPayload(self,content):
		self.payload = {
		"from":"zh",
		"to":"en",
		"query":content,
		"transtype":"realtime",
		"simple_means_flag":"3"
		}
		return self.payload
	#根据输入的参数查询其信息
	def query(self,content):
		self.mkPayload(content)
		r=requests.get(self.url,timeout=5,params=self.payload)
		r.raise_for_status()
		#print(r.encoding,r.apparent_encoding)
		r.encoding="utf-8"
		return json.loads(r.text)
	#用来暂时查看数据
	def writeInFile(self,data):
		f=open("a.txt","w",encoding='utf-8')
		f.write(data)
		f.close()
	#把查询到的数据整理
	def display(self,result):
		print(result["dict_result"])

		self.writeInFile(result)


def main():
	#要先获得用户输入的需要翻译的内容
	trans=Translate()
	while True:
		content=input("请输入要查询的内容,输入'退出'退出\n")
		if(content == "退出"):
			break
		result=trans.query(content)
		trans.display(result)


main()