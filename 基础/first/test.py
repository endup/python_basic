import time

print("开始计算")
time1=time.time()
for i in range(100000000):
	j=i
	k=i
	z=i
time2=time.time()

print("总共：",j+1,"\n用时：",time2-time1,"\n平均：",(j+1)/(time2-time1))
