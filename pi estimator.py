from tkinter import *
import random
import math

root = Tk()
#root.geometry("510x600")

canvas = Canvas(root, height=510, width=510, background="#2980b9",highlightbackground="#2980b9")
canvas.create_rectangle(10,10,500,500,width=1,outline="#f1c40f")
canvas.create_oval(10,10,500,500, outline= "#f1c40f", width=1)
canvas.grid(row = 0, columnspan=2)

text2 			= Label(root,text= "Closest Approximation:",bg="#3498db").grid(row=1,column=0,sticky=W+E+N+S)

text 			= Label(root,text = "0",bg="#3498db")
text.grid(row = 1, column=1,sticky=W+E+N+S)

text3 			= Label(root, text = "Current Approximation:",bg="#3498db").grid(row=2,column=0,sticky=W+E+N+S)

current 		= Label(root,bg="#3498db")
current.grid(row = 2, column=1,sticky=W+E+N+S)

iteration 		= Label(root,text = "Iteration:",bg="#3498db")
iteration.grid(row=3,column=0,sticky=W+E+N+S)

text4			= Label(root,bg="#3498db")
text4.grid(row = 3, column=1,sticky=W+E+N+S)


pointsincirlce 	= 0
closest			= [10,10]

def checkincircle(x,y):
	global pointsincirlce
	if math.sqrt((255-x)**2+(255-y)**2) > 245:
		return "#e74c3c"
	else:
		pointsincirlce += 1
		return "#27ae60"

def createpoint():
	rand 	= random.randint(10,500)
	rand2 	= random.randint(10,500)
	canvas.create_oval(rand-2,rand2-2,rand+2,rand2+2, fill = checkincircle(rand,rand2))
	canvas.grid(row = 0, column=0)
	root.update()
	return [rand,rand2]

for x in range(1,5001):
	createpoint()
	pi = (pointsincirlce/x)*4
	print(pi)
	if closest[1] > abs(math.pi-pi):
		closest = [pi,abs(math.pi-pi)]
		text.config(text = closest[0])
	current.config(text = pi)
	text4.config(text=x)
root.mainloop()

print("Closest:" + str(closest[0]))