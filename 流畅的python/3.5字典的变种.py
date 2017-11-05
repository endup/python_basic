import collections

ct=collections.Counter('aaasdssdsdddasadda')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(3))

#子类化UserDict
class StrkeyDict(collections.UserDict):
	def __missing__(self,key):
		if isinstance(key,str):
			raise KeyError(key)
		return self[str(key)]

	def __contains__(self,key):
		return str(key) in self.data
	#__setitem__ 会把所有的键都转换成字符串
	def __setitem__(self,key,item):
		self.data[str(key)]=item
#不可变映射类型
from types import MappingProxyType
d = {1:'A'}
#创建不可变的映射类型
d_proxy = MappingProxyType(d)
print(d_proxy,d_proxy[1])
#不能改变，但是它是动态的，对d的操作会映射到它上面
#d_proxy[2] = 'x'

d[2] = 'B'
print(d_proxy,d_proxy[2])