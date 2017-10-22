import requests
from bs4 import BeautifulSoup
import re
#pip install beautifulsoup4

r=requests.get("http://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
#print(demo)
soup=BeautifulSoup(demo,"html.parser")
#prettify()函数时在每个标签中添加换行，也就意味着只要是html格式的文本都能用它来美化
#print(soup.prettify())
print(soup.title)
#如果有多个则获取第一个
tag=soup.a
print(tag)
print(tag.name)
print(tag.parent.name)
print(tag.attrs)
print(tag.string)

#for link in soup.find_all('div'):  
	#print(link.get('class')) 
#print(soup.find_all(class_ = 'footer'))

#.contents 获得相应标签的树形结构，就是把每个其子节点信息分别作为一组元素
#.parent 父标签  .parents全部父标签
#.previous_sibling  前一个平行标签  .next_sibling  下一个平行标签
print(len(soup.head.contents))

#遍历子代
for child in soup.body.children:
	print(child)

#提取需要的内容
for link in soup.find_all("a"):
	print(link.get("href"))

print(soup.find_all(id=re.compile("k")))
print(soup.find_all(string=re.compile("class")))