from dis import dis

#dis.dis（反汇编函数）
print(dis('{1}'))
print("~~~~~~~~~~")
print(dis('set([1])'))

#集合推导
from unicodedata import name
a={chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
print(a)
