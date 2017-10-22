import requests


url="http://www.baidu.com/s"
a={"wd":"python"}
try:
	kv={"user-agent":"Mozilla/5.0"}
	r=requests.get(url,headers=kv,params=a)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.request.url)
	print(len(r.text))
except:
	print("爬取失败")