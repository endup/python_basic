import random
class BingoCage:

	def __init__(self, items):
		self._items = list(items)
		random.shuffle(self._items)
	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')
	#实现 __call__ 方法的类是创建函数类对象的简便方式
	def __call__(self):
		return self.pick()

bingo=BingoCage(range(5))
print(bingo.pick())
print(bingo())
print(callable(bingo))


#仅限关键字参数
def tag(name, *content, cls=None, **attrs):
	"""生成一个或多个HTML标签"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
		for attr, value
		in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
		(name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name="img"))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard','src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

print("-----------")
#operator模块
from functools import reduce
def fact(n):
	return reduce(lambda a, b: a*b, range(1, n+1))

from operator import mul
def fact2(n):
	return reduce(mul, range(1, n+1))
print(fact(5),fact2(5))

print("---------------")
metro_data = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

from operator import itemgetter
#，itemgetter(1) 的作用与 lambda fields:fields[1]
for city in sorted(metro_data, key=itemgetter(1)):
	print(city)
#如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组
cc_name = itemgetter(1, 0)
for city in metro_data:
	print(cc_name(city))
