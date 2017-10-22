
number=0
for num in range(0,100000):
	number+=1;
	print("\r当前速度：{:.2f}%".format(number*100/100000),end="")