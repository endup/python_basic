

cafe=bytes('cafeÂ',encoding='utf-8')
print(cafe)
print(cafe[0],cafe[:1])

cafe_arr=bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
print(cafe.decode('utf-8'))

#str中没有的方法.fromhex用来解析十六进制数字对
a=bytes.fromhex('31 4B CE A9')#可以考虑用在图片编码上
print(a.decode('utf-8'))

#用数组来初始化bytes
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)
#print(octets.decode('utf-8'))