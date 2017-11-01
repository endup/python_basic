
complex=4+5j
print(complex)
print(complex.real)
print(complex.imag)
#共轭复数
print(complex.conjugate())

#编码
str=u"helloworld"

out=str.encode("utf-8")
print(out)

dis=out.decode('utf-8')
print(dis)

#字典
dic={"a":"aaa","b":"bbb","c":"ccc"}
print(dic.items())
print(dic.keys())
print(dic.values())

#模拟二维数组(可以动态增加)
"""
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
d=[0,12,23,5]
e=[a,b,c,d]
print(e[0][2])
a.append(10)
print(e[0])
e[0][2]=12
print(a[2])
"""
#关于函数(一个*表示多个参数,两个表示把参数再存到字典中再传进去函数)
def test(a,b,*c):
	print(a)
	print(b)
	print("the number of c is :" ,len(c))
	print(c)
test(1,2)
test(1,2,3,4,5,6,7,8,9,10)

def test2(a,**b):
	print(a)
	print("the number of c is :" ,len(b))
	print(b)
test2(1,f=2,b=3,c=4,d=5,e=6)