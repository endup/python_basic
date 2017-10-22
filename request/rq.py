import requests
r=requests.get("http://www.baidu.com")
if(r.status_code==200):
	print(r.encoding)
	print(r.apparent_encoding)
	r.encoding=r.apparent_encoding
	#print(r.text)
	
	#print(r.content)
#params控制get请求的参数
a={"key1":"value1","key2":"value2"}
r1=requests.request("GET","http://www.baidu.com",params=a)
print(r1.url)
#data控制post请求的参数
#json
#cookies控制请求中的cookie
#auth元组，支持http认证功能
#files字典类型，传输文件
#timeout设置超时时间
#proxies设置代理
#allow_redirects设置是否允许重定向
#stream设置获取内容是否立即下载
#verify设置是否开启认证SSL证书
#cert本地SSL证书路径
#headers控制请求的头部信息
b={"user-agent":"Chrome/10"}
r2=requests.request("POST","http://www.baidu.com",headers=b)

c={"file":open("data.txt","rb")}
r3=requests.request("POST","http://www.baidu.com",files=c)


#通用代码框架
try:
	r=requests.get(url,timeout=30)
	#当返回的状态码不是200的时候抛出异常
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	return r.text
except:
	return "产生异常"