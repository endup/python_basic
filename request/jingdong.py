import requests
try:
	r=requests.get("https://red.jd.com/redIndex/16.html")
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[:1000])
except:
	print("爬取失败")