import requests

url="http://www.wechall.net/challenge/training/programming1/index.php?action=request"

head={
	"Cookie":"WC=9998976-38106-Huo3ZroXL4NhHXbL"
}

r=requests.get(url,headers=head)

url2="http://www.wechall.net/challenge/training/programming1/index.php?answer="+r.text



r2=requests.get(url2,headers=head)
print(r2.url)

#print(r2.text)