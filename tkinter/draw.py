from tkinter import *
import math as m

root=Tk()

w=Canvas(root,width=800,height=600)
w.pack()


#获取鼠标坐标
def paint(event):
	x1,y1=(event.x-1),(event.y-1)
	x2,y2=(event.x+1),(event.y+1)
	w.create_oval(x1,y1,x2,y2,fill="red")

w.bind("<B1-Motion>",paint)

Button(root,text="删除全部",command=(lambda x=ALL:w.delete(x))).pack()

mainloop()