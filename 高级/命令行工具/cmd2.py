import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument("-a","-b",action="count")
parser.add_argument("digital",type=int,nargs="*",help="多个以空格隔开的连续数字")
parser.add_argument("-sum",dest='sum',type=int,action="append",nargs="+",
						help="执行加法运算")
parser.add_argument("-multitude",dest='mul',type=int,action="append",nargs="+",
						help="执行乘法运算")
parser.add_argument("-s",dest='sea',action="append",nargs="+",
						help="搜索存活主机")
args = parser.parse_args()
if args.sum:
	j=0
	for i in args.sum[0]:
		j=j+i
	print("加法结果是：",j)
if args.mul:
	j=1
	for i in args.mul[0]:
		j=j*i
	print("乘法结果是：",j)
if args.sea:
	if len(args.sea[0])==1:
		print(args.sea[0][0],len(args.sea[0]))

#print(args)
