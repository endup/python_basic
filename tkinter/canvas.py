from tkinter import *

root=Tk()

w=Canvas(root,width=200,height=100)
w.pack()

line2=w.create_line(0,0,200,100,fill="blue",width=4)
line1=w.create_line(200,0,0,100,fill="red",dash=(4,4),width=3)
rect1=w.create_rectangle(40,20,160,80,fill="green")
rect2=w.create_rectangle(60,35,140,65,fill="yellow")

oval1=w.create_oval(60,35,140,65,fill="red")

text1=w.create_text(100,50,text="hello world!")

#删除对象
"""
w.coords(line1,0,25,200,25)
w.itemconfig(rect1,fill="black")
w.delete(line2)
"""

Button(root,text="删除全部",command=(lambda x=ALL:w.delete(x))).pack()

mainloop()