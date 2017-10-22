import pickle

data1=("ai",12,"fdafd","你好",[12,"fda"])
data2=["di",135,"封疆大吏",12]
data3={"a":123,"b":"bbbb"}

output1=open("data1.pkl","wb")
output2=open("data2.pkl","wb")
output3=open("data3.pkl","wb")

pickle.dump(data1,output1)
pickle.dump(data2,output2)
pickle.dump(data3,output3)

output1.close()
output2.close()
output3.close()

input1 = open('data1.pkl', 'rb')
input2 = open('data2.pkl', 'rb')
input3 = open('data3.pkl', 'rb')

data11=pickle.load(input1)
data22=pickle.load(input2)
data33=pickle.load(input3)

print(data11)
print(data22)
print(data33)

input1.close()
input2.close()
input3.close()