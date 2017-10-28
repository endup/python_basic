
#判断是否是素数
def isPrime(n): 
	if n <= 1: 
		return False
	if n == 2: 
		return True
	if n % 2 == 0: 
		return False
	i = 3
	while i * i <= n: 
		if n % i == 0: 
			return False
		i += 2
	return True

def main():
	for i in range(1000000,1000100):
		if(isPrime(i)):
			s=str(i)
			k=0
			#对素数的各个位的数字相加再判断是否为素数
			for j in s:
				k=k+int(j)
			if(isPrime(k)):
				print(i,k)

if __name__=="__main__":
	main()