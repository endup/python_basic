from tkinter import *

root=Tk()

frame=Frame(root)
frame.pack(padx=10,pady=10)

v1=StringVar()
v2=StringVar()
v3=StringVar()

def text(content):
	return content.isdigit()
def calc():
	result=int(v1.get())+int(v2.get())
	v3.set(str(result))

textCMD=root.register(text)

e1=Entry(frame,width=10,textvariable=v1,validate="key",validatecommand=(textCMD,'%P')).grid(row=0,column=0)
Label(frame,text="+").grid(row=0,column=1)

e2=Entry(frame,width=10,textvariable=v2,validate="key",validatecommand=(textCMD,'%P')).grid(row=0,column=2)
Label(frame,text="=").grid(row=0,column=3)

e3=Entry(frame,width=10,textvariable=v3,state="readonly").grid(row=0,column=4)

Button(frame,text="计算",command=calc).grid(row=1,column=2,pady=10)

mainloop()