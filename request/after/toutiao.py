import requests
from bs4 import BeautifulSoup
import bs4
import json

def getHTMLText(url):
	try:
		pyload={
			"offset":"0",
			"format":"json",
			"keyword":"食物",
			"autoload":"true",
			"count":"20",
			"cur_tab":"3"
		}
		r=requests.get(url,timeout=10,params=pyload)
		r.raise_for_status()
		return r.text
	except:
		return ""

def fillUnivList(ulist,html):
	#soup=BeautifulSoup(html,"html.parser")
	data=json.loads(html)
	if data and 'data' in data.keys():
		for item in data.get("data"):
			yield item.get("article_url")
	#writeinfile2(soup.prettify())
	#try:
	#ulist.append(soup.title.string.split("-")[0])
	#print(soup.title.string.split("-")[0])
	#except:
		#print("not found")

def main():
	uinfo=[]
	rootUrl="https://www.toutiao.com/search_content/"
	html=getHTMLText(rootUrl)
	for url in fillUnivList(uinfo,html):
		html2=getHTMLText(url)
	#writeinfile(uinfo)
	

def writeinfile(data):
	f=open("a.html","w",encoding='utf-8')
	for d in data:
		f.write(d+"\r\n")
	f.close()

def writeinfile2(data):
	f=open("a.html","w",encoding='utf-8')
	f.write(data+"\r\n")
	f.close()

main()