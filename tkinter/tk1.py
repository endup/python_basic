import tkinter as tk

'''
app=tk.Tk()
app.title("hello")

theLable=tk.Label(app,text="hello world!!!")
theLable.pack()

app.mainloop()'''

class App:
	def __init__(self,master):
		frame=tk.Frame(master)
		frame.pack(side=tk.LEFT,padx=100,pady=25)

		self.hi_there=tk.Button(frame,text="打招呼",bg="green",fg="blue",command=self.say_hi)
		self.hi_there.pack()

	def say_hi(self):
		print("hello")

root=tk.Tk()
app=App(root)

root.mainloop()
