

#oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wc osdlcodrlm.s
#换位密码

def switchE(str,times):
	tem=[]
	if len(str)/times ==0:
		ran=len(str)/times
	else:
		ran=int(len(str)/times)+1
	for i in range(ran):
		tem.append(str[i*times:(i+1)*times])
	res=""
	for o in range(times):
		for v in tem:
			try:
				res+=v[o]
			except:
				continue
	print(times,res)
	#print(times,res.split(" ")[0]," ",res.split(" ")[1],res.split(" ")[2])

def switchD(str,times):
	pass


def main():
	str="how are you ? i am fine,thank you"
	#str="oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wc osdlcodrlm.s"

	length=len(str)
	for i in range(length):
		i+=1
		switchE(str,i)
if __name__=="__main__":
	main()


