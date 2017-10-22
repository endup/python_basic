from tkinter import *
import math as m

root=Tk()

w=Canvas(root,width=200,height=100)
w.pack()

#画五角星
center_x=100
center_y=50
r=50

points=[
	#左上
	center_x-(r*m.sin(2*m.pi/5)),
	center_y-(r*m.cos(2*m.pi/5)),
	#右上
	center_x+(r*m.sin(2*m.pi/5)),
	center_y-(r*m.cos(2*m.pi/5)),
	#左下
	center_x-(r*m.sin(m.pi/5)),
	center_y+(r*m.cos(m.pi/5)),
	#顶点
	center_x,
	center_y-r,
	#右下
	center_x+(r*m.sin(m.pi/5)),
	center_y+(r*m.cos(m.pi/5)),
]

w.create_polygon(points,outline="red",fill="green")

Button(root,text="删除全部",command=(lambda x=ALL:w.delete(x))).pack()

mainloop()