from tkinter import *

root=Tk()

#定点菜单
mb=Menubutton(root,text="点击",relief=RAISED)
mb.pack()

#下拉列表框
option=[
	"1234",
	"2121",
	"dfaf",
	"21421"
]

variable=StringVar()
variable.set(option[0])

#w=OptionMenu(root,variable,"one","two","three")
w=OptionMenu(root,variable,*option)
w.pack()

def hello():
	print("hello")
def popup(event):
	thirdmenu.post(event.x_root,event.y_root)

menu=Menu(root)
#基础菜单
firstmenu=Menu(menu,tearoff=True)
firstmenu.add_command(label="hello",command=hello)
firstmenu.add_separator()
firstmenu.add_command(label="quit",command=root.quit)
menu.add_cascade(label="first",menu=firstmenu)

secondmenu=Menu(menu,tearoff=False)
secondmenu.add_command(label="hi",command=hello)
secondmenu.add_separator()
secondmenu.add_command(label="quit",command=root.quit)
menu.add_cascade(label="second",menu=secondmenu)

thirdmenu=Menu(menu,tearoff=False)
thirdmenu.add_command(label="hello world",command=hello)
thirdmenu.add_separator()
thirdmenu.add_command(label="quit",command=root.quit)

#点击右键弹出菜单
frame=Frame(root,width=500,height=400)
frame.pack()
frame.bind("<Button-3>",popup)

#多选菜单
helloVar=IntVar()
quitVar=IntVar()

forthmenu=Menu(menu,tearoff=True)
forthmenu.add_checkbutton(label="hello",command=hello,variable=helloVar)
forthmenu.add_separator()
forthmenu.add_checkbutton(label="quit",command=root.quit,variable=quitVar)
menu.add_cascade(label="forth",menu=forthmenu)

#单选菜单
fifVar=IntVar()

fifthmenu=Menu(menu,tearoff=True)
fifthmenu.add_radiobutton(label="hello",command=hello,variable=fifVar,value=1)
fifthmenu.add_separator()
fifthmenu.add_radiobutton(label="hello",command=hello,variable=fifVar,value=3)
fifthmenu.add_radiobutton(label="quit",command=root.quit,variable=fifVar,value=2)
menu.add_cascade(label="fifth",menu=fifthmenu)

#定点菜单

helloVar=IntVar()
quitVar=IntVar()

sixthmenu=Menu(mb,tearoff=True)
sixthmenu.add_checkbutton(label="hello",command=hello,variable=helloVar)
sixthmenu.add_separator()
sixthmenu.add_checkbutton(label="quit",command=root.quit,variable=quitVar)
#menu.add_cascade(label="forth",menu=forthmenu)

mb.config(menu=sixthmenu)
root.config(menu=menu)

mainloop()