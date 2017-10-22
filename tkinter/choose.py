from tkinter import *

root=Tk()

Cards=["J","Q","K","8"]

v=[]
#复选框
for card in Cards:
	v.append(IntVar())
	b=Checkbutton(root,text=card,variable=v[-1])
	b.pack(anchor="w")
#单选框
a=IntVar()
Radiobutton(root,text="one",variable=a,value=1).pack(anchor=W)
Radiobutton(root,text="two",variable=a,value=2).pack(anchor=W)
Radiobutton(root,text="three",variable=a,value=3).pack(anchor=W)

#循环创建单选框
words=[
	("hello",1),
	("today",2),
	("yesterday",3),
	("future",4)
]

#把选项包起来
group=LabelFrame(root,text="make a choose",padx=10,pady=10)
group.pack(padx=10,pady=10)

b=IntVar()
b.set(5)
for word,num in words:
	Radiobutton(group,text=word,variable=b,value=num,indicatoron=False).pack(fill=X)

mainloop()