import time
from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=200)
canvas.pack()

my_image=PhotoImage(file='ball.gif')
canvas.create_image(0,0,anchor=NW, image=my_image)
tk.mainloop()
