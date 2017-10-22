import requests
from bs4 import BeautifulSoup
import bs4
import json

#构造get请求url后面的参数
def makePar(page="1",verson="0",isFinish='0',startYear="0",tagID="",indexType="1",indexSort="0",area="",quarter="0"):
	par={
		"page":page,
		"page_size":"20",
		"version":verson,
		"is_finish":isFinish,
		"start_year":startYear,
		"tag_id":tagID,
		"index_type":indexType,
		"index_sort":indexSort,
		"area":area,
		"quarter":quarter
		}
	return par

#获取页数
def getPages(url,par=makePar()):
	try:
		r=requests.get(url,timeout=5,params=par)
		r.raise_for_status()
		data=json.loads(r.text)
		pages=data["result"]["pages"]
		return pages
	except:
		return ""
#获取页面数据
def getHTMLText(url,par=makePar()):
	try:
		r=requests.get(url,timeout=5,params=par)
		r.raise_for_status()
		return r.text
	except:
		return ""

#把获取的html转换成json
def transToData(html):
	data=json.loads(html)
	return data

def getInfo(html):
	#在这里对每部番进行详细信息的提取
	soup=BeautifulSoup(html,"html.parser")
	return soup

def main():
	#存放详细信息链接的列表
	moreInfo=[]
	rootUrl="https://bangumi.bilibili.com/web_api/season/index_global"
	#这里要选择好par
	par=makePar()
	pages=int(getPages(rootUrl,par))
	print("总页数：",pages)
	for i in range(pages+1):
		par=makePar(i+1)
		html=getHTMLText(rootUrl,par)
		data=transToData(html)
		writeinfile(data,moreInfo)
		print("读取第：",i+1,"页成功")
	#读取详细信息
	for url in moreInfo:
		html=getHTMLText(url)
		soup=getInfo(html)
		writeInMoreDetail(soup)
	print("成功完成数据的保存")


#把数据写入文件
def writeinfile(data,moreInfo):
	f=open("a.txt","a",encoding='utf-8')
	f.write("番剧名字\t\t封面图片网址\t\t\t\t追番人数\t总集数\t详细信息地址"+"\r\n")
	res=data["result"]["list"]
	for i in range(20):
		try:
			moreInfo.append(res[i]["url"])
			ma=res[i]["title"]+"\t"+res[i]["cover"]+"\t"+str(res[i]["favorites"])+"\t"+str(res[i]["total_count"])+"\t"+res[i]["url"]
			f.write(ma+"\r\n")
		except:
			f.close()
			break
	f.close()

def writeInMoreDetail(soup):
	f=open("b.txt","a",encoding="utf-8")

	title=soup.find(class_="info-title")
	print("名称:",title.string)
	onNum=soup.find(class_='info-count-item info-count-item-play')
	print("播放量：",onNum.em.string)
	cata=soup.find_all(class_="info-style-item")
	t=""
	for i in cata:
		t+=i.string+"."
	brief=soup.find(class_="info-desc")
	print("简介:",brief.string)
	info="名称:"+title.string+"\t播放量："+onNum.em.string+"\t"+t+"\t简介:"+brief.string+"\r\n"
	f.write(info)
	f.close()

main()