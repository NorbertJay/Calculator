import tkinter as tk
from tkinter import *
import math

root = tk.Tk()
root.title('Calculator')


canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()



buttons = tk.Frame(root, bg='white')
buttons.place(relwidth=1, relheight=.8, relx=0, rely=0.25)



b1=tk.Button(root, text = '7', padx=54, pady=25)
b1.place(x=10, y=140)

b2=tk.Button(root, text = '4', padx=54, pady=25)
b2.place(x=10, y=230)

b3=tk.Button(root, text = '1', padx=54, pady=25)
b3.place(x=10, y=320)

b4=tk.Button(root, text = '0', padx=54, pady=25)
b4.place(x=10, y=410)
#-------------------------------------------------------------
b5=tk.Button(root, text = '8', padx=54, pady=25)
b5.place(x=150, y=140)

b6=tk.Button(root, text = '5', padx=54, pady=25)
b6.place(x=150, y=230)

b7=tk.Button(root, text = '2', padx=54, pady=25)
b7.place(x=150, y=320)

b8=tk.Button(root, text = '.', padx=54, pady=25)
b8.place(x=150, y=410)
#-------------------------------------------------------------
b9=tk.Button(root, text = '9', padx=54, pady=25)
b9.place(x=289, y=140)

b10=tk.Button(root, text = '6', padx=54, pady=25)
b10.place(x=289, y=230)

b11=tk.Button(root, text = '3', padx=54, pady=25)
b11.place(x=289, y=320)

b12=tk.Button(root, text = '+', padx=54, pady=25)
b12.place(x=289, y=410)
#-----------------------------------------------------------------
b13=tk.Button(root, text='/', padx=25, pady=25)
b13.place(x=430, y=140)

b14=tk.Button(root, text='X', padx=25, pady=25)
b14.place(x=430, y=230)

b15=tk.Button(root, text='-', padx=25, pady=25)
b15.place(x=430, y=320)

b16=tk.Button(root, text='=', padx=25, pady=25)
b16.place(x=430, y=410)

root.mainloop()