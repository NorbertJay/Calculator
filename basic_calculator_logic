from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("650x400+300+300")

root.title("N2RCL Basic Calculator")

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

