import re
#面向对象式使用
pat=re.compile(r'\d')
print(pat.search("fda12hellowo231rld"))
#一次性操作
print(re.search(r"[0,1]\d\d|2[0-4]\d|25[0-5]",'200'))

print(re.search(r'((([0,1]{0,1}\d{0,1}\d|2{0,1}[0-4]{0,1}\d|2{0,1}5{0,1}[0-5])\.){3}([0,1]{0,1}\d{0,1}\d|2{0,1}[0-4]{0,1}\d|2{0,1}5{0,1}[0-5]))','198.10.23.2'))

print(re.search(r'<.+>','<html><title>hello</title></html>'))
#只要长度输出可能不同的，都可以通过在操作符后增加?变成最小匹配。
print(re.search(r'<.+?>','<html><title>hello</title></html>'))
"""
re.search(pattern, string, flags=0)
在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.I re.IGNORECASE 忽略正则表达式的大小写，[A‐Z]能够匹配小写字符
re.M re.MULTILINE 正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符


re.match()
从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()
搜索字符串，以列表类型返回全部能匹配的子串
re.split()
将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()
搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub(pattern, repl, string, count=2, flags=0)
在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
"""

#例子
import requests  
   
def getHTMLText(url):  
    try:  
        r = requests.get(url, timeout=30)  
        r.raise_for_status()  
        r.encoding = r.apparent_encoding  
        return r.text  
    except:  
        return ""  
          
def parsePage(ilt, html):  
    try:  
        #以列表类型返回全部能匹配的子串  
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)  
        #正则表达式的最小匹配  
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)  
        for i in range(len(plt)):  
            price = eval(plt[i].split(':')[1])  
            title = eval(tlt[i].split(':')[1])  
            ilt.append([price , title])  
    except:  
        print("出现异常")  
   
def printGoodsList(ilt):  
    tplt = "{:4}\t{:4}\t{:16}"  
    print(tplt.format("序号", "价格", "商品名称"))  
    count = 0  
    for g in ilt:  
        count = count + 1  
        print(tplt.format(count, g[0], g[1]))  
           
def main():  
    goods = '水杯'  
    depth = 3  
    start_url = 'https://s.taobao.com/search?q=' + goods  
    infoList = []  
    for i in range(depth):  
        try:  
            url = start_url + '&s=' + str(44*i)  
            html = getHTMLText(url)  
            parsePage(infoList, html)  
        except:  
            continue  
    printGoodsList(infoList)  
       
main()  