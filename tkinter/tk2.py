import tkinter as tk

def callback():
	var.set("to be!!!")

root=tk.Tk()

frame1=tk.Frame(root)
frame2=tk.Frame(root)

#设置text内容
var=tk.StringVar()
var.set("to be or not to be\nit is a question")
textLabel=tk.Label(frame1,
					textvariable=var,
					justify=tk.LEFT)#左对齐
textLabel.pack(side=tk.LEFT)

photo=tk.PhotoImage(file="1.gif")
imgLabel=tk.Label(frame1,image=photo)
imgLabel.pack(side=tk.RIGHT)

#点击按钮调用command
button=tk.Button(frame2,text="to be!!",command=callback)
button.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
#文字显示在图片上
"""
photo2=tk.PhotoImage(file="1.gif")
tLabel=tk.Label(root,
				text="hello",
				justify=tk.LEFT,
				image=photo2,
				compound=tk.CENTER,
				font=("微软雅黑",20),
				fg="black")
tLabel.pack()
"""
root.mainloop()

