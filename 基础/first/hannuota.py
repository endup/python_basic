def han(n,a,b,c):
  if(n<1):
    print("unknow false")
    return -1
  if(n==1):
#把最后一个移动到c
    print(a,"-->",c)
    #print("over")
    return 1
  else:
#把n-1个移动到b
    han(n-1,a,c,b)
#把最后一个移动到c
    print(a,"-->",c)
#把n-1个移动到c
    han(n-1,b,a,c)

result=han(3,"a","b","c")
print(result)