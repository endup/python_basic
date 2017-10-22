import requests

try:
	kv={"user-agent":"Mozilla/5.0"}
	r=requests.get("https://www.amazon.cn/dp/B0761LYM2Z",headers=kv)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[:1000])
except:
	print("爬取失败")