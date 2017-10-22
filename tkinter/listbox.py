from tkinter import *

root=Tk()

#滚动条
sr=Scrollbar(root)
sr.pack(side=RIGHT,fill=Y)

#选项单,yscrollcommand=sr.set设置滚动条
listBox=Listbox(root,yscrollcommand=sr.set,selectmode=EXTENDED,height=20)
listBox.pack(side=LEFT,fill=BOTH)
#让滚动条跟随选项单
sr.config(command=listBox.yview)

for item in range(200):
	listBox.insert(END,item)
#删除按钮
button=Button(root,text="删除",command=lambda x=listBox:x.delete(ACTIVE))
button.pack()

#滑块
s1=Scale(root,from_=0,to=50)
s1.pack()
s2=Scale(root,from_=0,to=200,orient=HORIZONTAL)
s2.pack()

def show():
	print(s1.get(),s2.get())

Button(root,text="获取滑块位置",command=show).pack()

mainloop()