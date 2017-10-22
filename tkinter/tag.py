from tkinter import *
import webbrowser

root=Tk()

def show_arrow_cursor(event):
	text.config(cursor="arrow")
def show_xterm_cursor(event):
	text.config(cursor="xterm")
def click(event):
	webbrowser.open("http://www.baidu.com")
def callback(event):
	text.edit_separator()
def show():
	text.edit_undo()
#undo=True,autoseparators=False,设置可撤销，不自动添加分割符
text=Text(root,width=30,height=5,undo=True,autoseparators=False)
text.pack()
#当text中的内容改变时调用callback
text.bind("<Key>",callback)

text.insert(INSERT,"to be or not to be\n")
text.insert(INSERT,"www.baidu.com")
#用tag来修改字体属性
text.tag_add("tag1","1.7","1.12","1.15")
text.tag_config("tag1",background="blue",foreground="black")
#给文字添加事件
text.tag_add("link","2.3","2.9")
text.tag_config("link",foreground="blue",underline=True)
text.tag_bind("link","<Enter>",show_arrow_cursor)
text.tag_bind("link","<Leave>",show_xterm_cursor)
text.tag_bind("link","<Button-1>",click)

#撤销
Button(root,text="撤销",command=show).pack()

mainloop()