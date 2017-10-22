import urllib.request

#这是个查询ip地址的网站
url="http://www.whatismyip.coml.tw/"
proxy_support=urllib.request.ProxyHandler({"http":"61.135.217.7:80"})
#创建
opener=urllib.request.build_opener(proxy_support)
#安装
urllib.request.install_opener(opener)
#调用
response=urllib.request.urlopen(url)
html=response.read().decode("utf-8")

print(html)
