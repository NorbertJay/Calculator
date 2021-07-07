from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("650x400+300+300")

root.title("N2RCL Basic Calculator")
root.minsize(650,400)

switch = None


class Calculator:

    # These functions are for numbers (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) buttons when pressed
    
    def btn1_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "1")

    def btn2_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "2")

    def btn3_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "3")

    def btn4_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "4")

    def btn5_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "5")

    def btn6_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "6")

    def btn7_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "7")

    def btn8_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "8")

    def btn9_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "9")

    def btn0_pressed(c):
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "0")

    # For binding the keys in the keyboard
    def key_event(c, *args):
        if disp.get() == '0':
            disp.delete(0, END)
            
            
    # These functions are for operational symbols (+, -, x, /) buttons when pressed
    
    def btnplus_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, "+")
    
    def btnminus_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, "-")

    def btnmultiply_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, "*")

    def btndivide_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, "/")
        
        
    # These functions are for the symbols (dot, clear, delete, equals) buttons when pressed
   
    def btndot_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, ".")

    def btnclear_pressed(c, *args):
        disp.delete(0, END)
        disp.insert(0, "0")

    def btndelete_pressed(c):
        pos = len(disp.get())
        display = str(disp.get())
        if display == " ":
            disp.insert(0, "0")
        elif display == " ":
            disp.insert(0, "0")
        elif display == "0":
            pass
        else:
            disp.delete(0, END)
            disp.insert(0, display[0:pos-1])

    def btnequal_pressed(c, *args):
        try:
            ans = disp.get()
            ans = eval(ans)
            disp.delete(0, END)
            disp.insert(0, ans)
            return str(ans)
        except:
            tkinter.messagebox.showerror("Value Error", "Make sure your values and operators are correct")

    def run(c):
        root.mainloop()

# Code for Calculator UI Here
# Attempt sa Calculator UI
c = Calculator()

display_widget = StringVar()

disp = Entry(root, text="DISPLAY BAR IS HERE", font="Arial 35", fg="black", bg="white", bd=0, justify=RIGHT, insertbackground="white", cursor="arrow")
disp.pack(expand=TRUE, fill=BOTH)
disp.insert(0, '0')
disp.focus_set()

# To bind/connect to keyboard
disp.bind("<Return>", c.btnequal_pressed)
disp.bind("<Escape>", c.btnclear_pressed)
disp.bind("<Key-1>", c.key_event)
disp.bind("<Key-2>", c.key_event)
disp.bind("<Key-3>", c.key_event)
disp.bind("<Key-4>", c.key_event)
disp.bind("<Key-5>", c.key_event)
disp.bind("<Key-6>", c.key_event)
disp.bind("<Key-7>", c.key_event)
disp.bind("<Key-8>", c.key_event)
disp.bind("<Key-9>", c.key_event)
disp.bind("<Key-0>", c.key_event)
disp.bind("<Key-.>", c.key_event)


# Calculator UI

# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Arial 23", relief=GROOVE, bd=0, command=c.btn1_pressed, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Arial 23", relief=GROOVE, bd=0,  command=c.btn2_pressed, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Arial 23", relief=GROOVE, bd=0, command=c.btn3_pressed, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Arial 23", relief=GROOVE, bd=0, command=c.btnplus_pressed, fg="white", bg="#333333")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)


btn4 = Button(btnrow2, text="4", font="Arial 23", relief=GROOVE, bd=0, command=c.btn4_pressed, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Arial 23", relief=GROOVE, bd=0, command=c.btn5_pressed, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Arial 23", relief=GROOVE, bd=0, command=c.btn6_pressed, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Arial 23", relief=GROOVE, bd=0, command=c.btnminus_pressed, fg="white", bg="#333333")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Arial 23", relief=GROOVE, bd=0, command=c.btn7_pressed, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Arial 23", relief=GROOVE, bd=0, command=c.btn8_pressed, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Arial 23", relief=GROOVE, bd=0, command=c.btn9_pressed, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Arial 23", relief=GROOVE, bd=0, command=c.btnmultiply_pressed, fg="white", bg="#333333")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Arial 21", relief=GROOVE, bd=0, command=c.btndot_pressed, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Arial 23", relief=GROOVE, bd=0, command=c.btn0_pressed, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="DEL", font="Arial 15", relief=GROOVE, bd=0, command=c.btndelete_pressed, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Arial 23", relief=GROOVE, bd=0, command=c.btndivide_pressed, fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

btnclear = Button(btnrow5, text="AC", font="Arial 15", relief=GROOVE, bd=0, command=c.btnclear_pressed, fg="white", bg="#333333")
btnclear.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnequal = Button(btnrow5, text="=", font="Arial 23", relief=GROOVE, bd=0, command=c.btnequal_pressed, fg="white", bg="#333333")
btnequal.pack(side=LEFT, expand=TRUE, fill=BOTH)




if __name__ == "__main__":
    c.run()


