import urllib.request
import urllib.parse
import json
import time

def trans(src):
	url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	data={
		"i":src,
		"from":"AUTO",
		"to":"AUTO",
		"smartresult":"dict",
		"client":"fanyideskweb",
		#"salt":"1506391258396",
		#"sign":"ce0bb64e79781a1495a24182ffc0d724",
		"doctype":"json",
		"version":"2.1",
		"keyfrom":"fanyi.web",
		"action":"FY_BY_CLICKBUTTION",
		"typoResult":"true",
	}
	data=urllib.parse.urlencode(data).encode("utf-8")

	response=urllib.request.urlopen(url,data)
	html=response.read().decode("utf-8")

	target=json.loads(html)
	src=target["translateResult"][0][0]['src']
	tgt=target["translateResult"][0][0]['tgt']
	print("要翻译的内容:%s" % src)
	print("翻译结果:%s" % tgt)

	time.sleep(1)


head={
	#"Accept-Encoding":"gzip, deflate",
	#"Accept-Language":"zh-CN,zh;q=0.8",
	#"Connection":"keep-alive",
	#"Content-Length":"244",
	#"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	#"Cookie":"DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-564676419@183.63.79.36; JSESSIONID=abcg0siV78QyvfFav676v; OUTFOX_SEARCH_USER_ID_NCOO=50710227.234950684; _ntes_nnid=7dcdc94cdea6efd7e24c891b12ffb1b6,1506391210376; ___rl__test__cookies=1506392006112",
	#"Host":"fanyi.youdao.com",
	#"Origin":"http://fanyi.youdao.com",
	#"Referer":"http://fanyi.youdao.com/?keyfrom=dict2.top",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
	#"X-Requested-With":"XMLHttpRequest"
}
while 1:
	print("请输入要查询的中文或英文,输入qit退出")
	src=input()
	if(src=="qit"):
		break
	if(src):
		trans(src)