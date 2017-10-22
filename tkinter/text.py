from tkinter import *

root=Tk()

text=Text(root,width=30,height=20)
text.pack()

text.insert(INSERT,"hello world\n")
text.insert(END,"here you are")

photo=PhotoImage(file="1.gif")

def show():
	text.image_create(END,image=photo)
	print("插入了一张图片")

b1=Button(text,text="点击有惊喜",command=show)
#在text中插入botton
text.window_create(INSERT,window=b1)

mainloop()