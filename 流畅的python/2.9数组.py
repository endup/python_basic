from array import array
from random import random
import time

time1=time.time()
floats=array('d',(random() for i in range(10**7)))
time2=time.time()
print("创建一个一千万的浮点数数组耗时:",time2-time1)
print(floats[-1])
fp=open('floats.bin','wb')
#.tofile,.fromfile是array的特有方法，快速的对文件存取
floats.tofile(fp)
time3=time.time()
print("把一千万个浮点数写入文件耗时:",time3-time2)
fp.close()

time6=time.time()
for i in floats:
	i/=3.0
time7=time.time()
print("对数组中的一千万个浮点数进行计算耗时:",time7-time6)

floats2=array('d')
fp=open('floats.bin','rb')
time4=time.time()
floats2.fromfile(fp,10**7)
time5=time.time()
print("把一千万个浮点数从文件读取耗时:",time5-time4)
fp.close()

print(floats2[-1])
print(floats==floats2)

#memoryview对象
numbers=array('h',[-2,-1,0,1,2])
print(numbers)
memv=memoryview(numbers)
print(len(memv))

print(memv[0])
memv_oct=memv.cast('B')
print(memv_oct.tolist())
#把占 2 个字节的整数的高位字节改成4
memv_oct[5]=4
print(numbers)

#队列
from collections import deque
#maxlen是可选参数，一旦确定就不能更改
dq=deque(range(10),maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(55)
print(dq)
dq.extend([11,22,33])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)
#append 和 popleft 都是原子操作，也就说是 deque 可以在多线程程序
#中安全地当作先进先出的栈使用，而使用者不需要担心资源锁的问题。