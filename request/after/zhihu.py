import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		kv={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Cookie":"aliyungf_tc=AQAAAPc8dFBeng0AM9f4OlG7NM0dOAgt; q_c1=4b052687bd304c658f2755e0993d4fc6|1508487280000|1508487280000; q_c1=b85f626663b241599b66607bae399000|1508487280000|1508487280000; _zap=d1e33e8f-a30b-4bc4-92e5-a2d5a91a17bd; __utma=155987696.776995932.1508488150.1508488150.1508488150.1; __utmb=155987696.0.10.1508488150; __utmc=155987696; __utmz=155987696.1508488150.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); l_n_c=1; l_cap_id='YWIzNjkzYzg3ZmMwNDczZmJhOWVjMjIwNmE2ODFiMTQ=|1508488308|e0850970202e631293cf61abe9cb0bfce72f4468'; r_cap_id='OTdiNTg5ODIwOTFmNGM4Njk3YTMxNTZlMTg4ZmQ4MmQ=|1508488308|cb3cc64358d0430a8e8c6a8d93377d27a87a8eb2'; cap_id='OTU5ZGRmZTg3OWMxNDYzNjkyNjI1OTgzYTFiNTZlM2Y=|1508488308|4e6b5d6e704c2ee6b1d18a694b14c84dd1759702'; n_c=1; _xsrf=40a61b9e-7fd4-437e-b693-c8fbf31549e0",
		"Host":"www.zhihu.com",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
		}
		r=requests.get(url,headers=kv,timeout=1)
		r.raise_for_status()
		#print(r.encoding,r.apparent_encoding)
		#r.encoding=r.apparent_encoding
		#print(r.text)
		return r.text
		
	except:
		return ""

def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	#writeinfile2(soup.prettify())
	try:
		ulist.append(soup.title.string.split("-")[0])
		print(soup.title.string.split("-")[0])
	except:
		print("not found")

def main():
	uinfo=[]
	rootUrl="https://www.zhihu.com/question/"
	j=19550225
	for i in range(20000000):
		addi='%d' %(j+i)
		url=rootUrl+addi
		html=getHTMLText(url)
		fillUnivList(uinfo,html)
	writeinfile(uinfo)
	

def writeinfile(data):
	f=open("a.txt","w",encoding='utf-8')
	for d in data:
		f.write(d+"\r\n")
	f.close()

def writeinfile2(data):
	f=open("a.txt","w",encoding='utf-8')
	f.write(data+"\r\n")
	f.close()

main()