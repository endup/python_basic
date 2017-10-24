import pickle

d=dict(name='bob',age=20,score=18)
a=pickle.dumps(d)
print(a)

f=open("dump.txt","wb")
pickle.dump(d,f)
f.close()

with open("dump.txt","rb") as f:
	e=pickle.load(f)
print(e)