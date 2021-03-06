# Code for Calculator UI Here
# Attempt sa Calculator UI

from tkinter import *
import math

root = Tk()
root.geometry("650x400+300+300")
root.title("Calculator")
switch = None
root.minsize(650,400)


display_widget = StringVar()

disp = Entry(root, text="DISPLAY BAR IS HERE", font="Arial 35", fg="black", bg="white", bd=0, justify=RIGHT, insertbackground="white", cursor="arrow")
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Arial 23", relief=GROOVE, bd=0,   fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)


btn4 = Button(btnrow2, text="4", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" ??? ", font="Arial 21", relief=GROOVE, bd=0,  fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="DEL", font="Arial 15", relief=GROOVE, bd=0,  fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Arial 23", relief=GROOVE, bd=0,  fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

btnclear = Button(btnrow5, text="AC", font="Arial 15", relief=GROOVE, bd=0, fg="white", bg="#333333")
btnclear.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnequal = Button(btnrow5, text="=", font="Arial 23", relief=GROOVE, bd=0, fg="white", bg="#333333")
btnequal.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
