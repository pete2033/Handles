from tkinter import *
from tkinter import ttk

root = Tk()
root.title("handles test")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

placetopleft=ttk.Entry(mainframe, width=20, textvariable=StringVar())
placetopleft.grid(column=1, row=1, sticky=(N, W, E, S))
topright=ttk.Entry(mainframe, width=20, textvariable=StringVar())
middlemiddle=ttk.Label(mainframe, width=20, text="test1")
middlemiddle.grid(column=2, row=2, sticky=(N, W, E, S))
bottomright=ttk.Label(mainframe, width=20, text="test")
bottomright.grid(column=3, row=3, sticky=(N, W, E, S))

canvas= Canvas(mainframe, width=500, height=500, bg="white")
canvas.create_oval(10, 10, 200, 200, fill="lightblue", outline="grey")
canvas.create_oval(310, 10, 500,200, fill="lightblue",outline="grey" )
#canvas.create_rectangle(60, 200, 10, 150, fill="lightblue", outline="grey")
canvas.create_polygon(20,200,20,150,20,100, 50, 100, 50,200, fill="lightblue", outline="grey")

canvas.grid(column=1, row=4, sticky=(N, W, E, S))

root.mainloop()

