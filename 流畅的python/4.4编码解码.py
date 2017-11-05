
city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))

#print(city.encode('cp437'))
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
#print(octets.decode('utf_8'))
print(octets.decode('utf_8', errors='replace'))
print("~~~~~~~~~~~~~~~~~~~~~~~~")

#探索编码默认值
import sys, locale
expressions = """
	locale.getpreferredencoding()
	type(my_file)
	my_file.encoding
	sys.stdout.isatty()
	sys.stdout.encoding
	sys.stdin.isatty()
	sys.stdin.encoding
	sys.stderr.isatty()
	sys.stderr.encoding
	sys.getdefaultencoding()
	sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expression in expressions.split():
	value = eval(expression)
	print(expression.rjust(30), '->', repr(value))
