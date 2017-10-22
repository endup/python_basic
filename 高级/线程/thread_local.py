import threading

local_school=threading.local()
num=0

def test1():
	local_school.student=0
	global num
	for i in range(1000000):
		local_school.student+=1
		num+=1
	print("test1",local_school.student,"!!",num)


def test2():
	local_school.student=0
	global num
	for i in range(1000000):
		local_school.student+=1
		num+=1
	print("test2",local_school.student,"@@@",num)




t1=threading.Thread(target=test1)
t1.start()

t2=threading.Thread(target=test2)
t2.start()

	