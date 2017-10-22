from tkinter import *

root=Tk()

def create():
	top=Toplevel()
	#top.attributes("-alpha",0.5)
	top.title("click")
	msg=Message(top,text="hello")
	msg.pack()
		

m1=PanedWindow(showhandle=True,sashrelief=SUNKEN)
m1.pack(fill=BOTH,expand=1)

left=Label(m1,text="left pane")
m1.add(left)

#orient=VERTICAL垂直分布，默认水平
m2=PanedWindow(orient=VERTICAL,showhandle=True,sashrelief=SUNKEN)
m1.add(m2)

top=Label(m2,text="top")
m2.add(top)

Button(top,text="点击弹窗",command=create).pack()

bottom=Label(m2,text="top")
m2.add(bottom)

mainloop()