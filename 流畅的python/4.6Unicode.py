from unicodedata import normalize

s1='café'
s2 = 'cafe\u0301'

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

#NFC默认大小写不相等
print(normalize('NFD','A') == normalize('NFD','a'))
#但是也可以再加个函数来控制大小写重叠
print(normalize('NFD','A').casefold() == normalize('NFD','a').casefold())
