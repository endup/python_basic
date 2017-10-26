import struct

"""
参数含义
http://images.cnblogs.com/cnblogs_com/coser/201112/201112171613441943.png
x 
c	char	字符串长度	1
b	signed	char	1
B
?
h
H
i
I
l
L
q
Q
f
d
s
P
p
"""
#字节顺序
#http://images.cnblogs.com/cnblogs_com/coser/201112/20111217161345373.png

packed=struct.pack('>IH',123456,65500)
print(packed)

unpacked=struct.unpack('>IH',packed)
print(unpacked)

#windows的位图文件.bmp的前30个字节
"""
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
"""
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
bmp=struct.unpack('<ccIIIIIIHH', s)
print(bmp)