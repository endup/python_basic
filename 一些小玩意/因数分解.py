import requests
from bs4 import BeautifulSoup
#对一个大数进行因素分解，感觉效率不够
url="http://www.wechall.net/challenge/impossible/index.php?request=new_number"

r=requests.get(url)
soup=BeautifulSoup(r.text)

tarNum=soup.select('#page')[0].string.split()[0]

#一个不断产生素数的迭代器
def createPrime():
	#yield 1
	yield 2
	i=3
	while True:
		if(isPrime(i)):
			yield i
			i+=2
		else:
			i+=2

#判断数字是否为素数
def isPrime(n): 
	i = 3
	while i * i < n: 
		if n % i == 0: 
			return False
		i += 2
	return True


#对目标数字进行因素分解
def decomposed(num):
	res=""
	for i in createPrime():
		if (num%i==0):
			res+=i
			num=num/i	
			print("i")
		if(i>500000000):
			return res
			break


def f(n):  
    n=int(n)
    res=""
    for i in range(2,int(n/2)+1):  
        if n%i==0: 
            res+=str(i)
            print(res)
            #print (i)  
            #print ("*",)  
            return f(n/i)  
    return res


#print(int(tarNum),"!!!!!!!!!!")

#value=decomposed(int(tarNum))
value=f(int(9000000000000000000000000000000))
print(value)
