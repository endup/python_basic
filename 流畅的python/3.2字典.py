import collections

#创建字典的不同方式
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

#元组
DIAL_CODES = [
	(86, 'China'),
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
	(55, 'Brazil'),
	(92, 'Pakistan'),
	(880, 'Bangladesh'),
	(234, 'Nigeria'),
	(7, 'Russia'),
	(81, 'Japan'),
]
#元组转换成字典
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
f={code: country.upper() for country, code in country_code.items()
if code < 66}
print(f)
print(country_code)

#.defaultdict是用来给字典一些没定义的key默认value值以防抛出错误
dd=collections.defaultdict(dict)
print(dd[12])

#继承dict类通过__missing__方法来让字典支持key为数字
class StrKeyDict(dict):
	def __missing__(self, key):
		#判断找不到的key是否是str
		if isinstance(key, str):
			#key是str则说明字典中没有这个值
			raise KeyError(key)
		#key不是str则转换成str再查询一次
		return self[str(key)]
	def get(self, key, default=None):
		try:
			return self[key]
		except KeyError:
			return default
	def __contains__(self, key):
		#对应in操作符
		return key in self.keys() or str(key) in self.keys()

d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'],d[4])
#print(d[1])

print(d.get('2'),d.get(4))
print(d.get(1,'N/A'))

print(2 in d)
print(1 in d)
