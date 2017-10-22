import urllib.request
import os
import random
import re
import time

#打开链接
def url_open(url):
	req=urllib.request.Request(url)
	headers={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		#"Host":"ws4.sinaimg.cn",
		"Upgrade-Insecure-Requests":"1",
		"If-Modified-Since":"Mon, 08 Jul 2013 18:06:40 GMT",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
	}
	#req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")"
	#req.add_header("Upgrade-Insecure-Requests","1")
	'''
	#设置代理
	proxies=["111.13.7.42:81"]
	proxy=random.choice(proxies)

	proxy_support=urllib.request.ProxyHandler({"http":proxy})
	opener=urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	'''
	#获取连接数据
	headers=urllib.parse.urlencode(headers).encode("utf-8")

	response=urllib.request.urlopen(url,headers)
	html=response.read()
	return html

#获取页面中的page
def get_page(url):
	html=url_open(url).decode('utf-8')

	a=re.search(r'<span class="current-comment-page">\[(.+?)\]</span>',html)

	return a.group(1)

#从页面中抓取img链接
def find_img(url):
	html=url_open(url).decode('utf-8')
	img_address=[]
	a=re.findall(r'<img src="(.+?)[^r][^p][^g].jpg"',html)
	for i in a:
		img_address.append("http:"+i+".jpg")
	return img_address

#把img保存起来
def save_img(folder,each):
		filename=each.split("/")[-1]
		with open(filename,"wb") as f:
			img=url_open(each)
			f.write(img)


def download_pto(folder='folder',pages=300):
	#新建存储的目录
	os.mkdir(folder)
	os.chdir(folder)
	os.mkdir("0")
	os.chdir("0")

	url="http://jandan.net/ooxx/"
	a=0
	b=0
	page_num=int(get_page(url))
	for i in range(pages):
		page_num-=1
		page_url=url+"page-"+str(page_num)+"#comments"
		img_address=find_img(page_url)
		for each in img_address:
			if(a>=200):
				b+=1
				os.chdir('../')
				os.mkdir(str(b))
				os.chdir(str(b))
				a=0
			print(a,b,each)
			a+=1
			save_img(str((b-1)),each)

if __name__=='__main__':
	download_pto()