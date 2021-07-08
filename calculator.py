from tkinter import *
import tkinter.messagebox
import math


root = Tk()
root.geometry("650x400+300+300")

root.title("Calculator by N2RCL")
root.minsize(650,400)

switch = None


# Functions for pressing the buttons

class Calculator:

    # These functions are for number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) buttons when pressed

    def btn1_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '1')


    def btn2_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '2')


    def btn3_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '3')


    def btn4_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '4')


    def btn5_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '5')


    def btn6_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '6')


    def btn7_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '7')


    def btn8_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '8')


    def btn9_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '9')


    def btn0_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '0')


    # This function is for binding the buttons to the keyboard

    def key_event(c, *args):
        if disp.get() == '0':
            disp.delete(0, END)

    
    # These functions are for operational symbols (+, -, x, /) buttons when pressed

    def btnplus_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '+')


    def btnminus_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '-')


    def btnmultiply_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '*')


    def btndivide_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '/')


    # These functions are for trigonometric operations (sin, cos, tan, arcsin, arccos, arctan) buttons when pressed

    def sin_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.sin(math.radians(ans))
            else:
                ans = math.sin(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def cos_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.cos(math.radians(ans))
            else:
                ans = math.cos(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def tan_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.tan(math.radians(ans))
            else:
                ans = math.tan(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def arcsin_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.degrees(math.asin(ans))
            else:
                ans = math.asin(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def arccos_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.degrees(math.acos(ans))
            else:
                ans = math.acos(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def arctan_pressed(c):
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.degrees(math.atan(ans))
            else:
                ans = math.atan(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    # These functions are for additional operations (exponents, logarithm, ln, factorial, square root, round) buttons when pressed

    def pow_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '**')


    def round_pressed(c):
        try:
            ans = float(disp.get())
            ans = round(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def logarithm_pressed(c):
        try:
            ans = float(disp.get())
            ans = math.log10(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def fact_pressed(c):
        try:
            ans = float(disp.get())
            ans = math.factorial(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def sqrt_pressed(c):
        try:
            ans = float(disp.get())
            ans = math.sqrt(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    # These functions are for dot ".", pi, natural log (ln), natural number (e), convert (Radian & Degress), open (bl) & close(br) brackets, and Remainder integer (Modulo) buttons when pressed
    def dot_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '.')


    def pi_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        ans = math.pi
        disp.insert(pos, ans)
        return str(ans)


    def e_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        ans = math.e
        disp.insert(pos, ans)
        return str(ans)


    def bl_pressed(c):
        if disp.get() == '0':
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, '(')


    def br_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, ')')


    def conv_pressed(c):
        global switch
        if switch is None:
            switch = True
            conv_btn['text'] = "Deg"
        else:
            switch = None
            conv_btn['text'] = "Rad"


    def ln_pressed(c):
        try:
            ans = float(disp.get())
            ans = math.log(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
            return str(ans)
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")


    def mod_pressed(c):
        pos = len(disp.get())
        disp.insert(pos, '%')

    # These functions are for delete, clear(AC) and equal buttons when pressed

    def del_pressed(c):
        pos = len(disp.get())
        display = str(disp.get())
        if display == '':
            disp.insert(0, '0')
        elif display == ' ':
            disp.insert(0, '0')
        elif display == '0':
            pass
        else:
            disp.delete(0, END)
            disp.insert(0, display[0:pos-1])
    
    def btnclear_pressed(c, *args):
        disp.delete(0, END)
        disp.insert(0, '0')

    def btnequal_pressed(c, *args):
        try:
            ans = disp.get()
            ans = eval(ans)
            disp.delete(0, END)
            disp.insert(0, ans)
            return str(ans)
        except:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    
    def run(c):
        root.mainloop()


#CALCULATOR UI

# Display Widget, This is what will be displayed in the label/screen ng calculator

c = Calculator()

display_widget = StringVar()

disp = Entry(root, font="Arial 25", fg="black", bg="white", bd=0, justify=RIGHT, insertbackground="white", cursor="arrow")
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# For binding in buttons in the keyboard
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

pi_btn = Button(btnrow1, text="π", font="Arial 18", relief=GROOVE, bd=0, command= c.pi_pressed, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Arial 18", relief=GROOVE, bd=0, command=c.fact_pressed, fg="white", bg="#333333")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Arial 18", relief=GROOVE, bd=0, command=c.sin_pressed, fg="white", bg="#333333")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Arial 18", relief=GROOVE, bd=0, command=c.cos_pressed, fg="white", bg="#333333")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Arial 18", relief=GROOVE, bd=0, command=c.tan_pressed, fg="white", bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

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

e_btn = Button(btnrow2, text="e", font="Arial 18", relief=GROOVE, bd=0, command=c.e_pressed, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Arial 18", relief=GROOVE, bd=0, command=c.sqrt_pressed, fg="white", bg="#333333")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Arial 11 bold", relief=GROOVE, bd=0, command=c.arcsin_pressed, fg="white", bg="#333333")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Arial 11 bold", relief=GROOVE, bd=0, command=c.arccos_pressed, fg="white", bg="#333333")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Arial 11 bold", relief=GROOVE, bd=0, command=c.arctan_pressed, fg="white", bg="#333333")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

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

conv_btn = Button(btnrow3, text="Rad", font="Arial 12 bold", relief=GROOVE, bd=0, command=c.conv_pressed, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Arial 10 bold", relief=GROOVE, bd=0, command=c.round_pressed, fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Arial 18", relief=GROOVE, bd=0, command=c.ln_pressed, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Arial 17", relief=GROOVE, bd=0, command=c.logarithm_pressed, fg="white", bg="#333333")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Arial 17", relief=GROOVE, bd=0, command=c.pow_pressed, fg="white", bg="#333333")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

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

mod_btn = Button(btnrow4, text="%", font="Arial 21", relief=GROOVE, bd=0, command=c.mod_pressed, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Arial 21", relief=GROOVE, bd=0, command=c.bl_pressed, fg="white", bg="#333333")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Arial 21", relief=GROOVE, bd=0, command=c.br_pressed, fg="white", bg="#333333")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Arial 21", relief=GROOVE, bd=0, command=c.dot_pressed, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnclear = Button(btnrow4, text="AC", font="Arial 15", relief=GROOVE, bd=0, command=c.btnclear_pressed, fg="white", bg="#333333")
btnclear.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="DEL", font="Arial 15", relief=GROOVE, bd=0, command=c.del_pressed, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Arial 23", relief=GROOVE, bd=0, command=c.btn0_pressed, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnequal = Button(btnrow4, text="=", font="Arial 23", relief=GROOVE, bd=0, command=c.btnequal_pressed, fg="white", bg="#333333")
btnequal.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Arial 23", relief=GROOVE, bd=0, command=c.btndivide_pressed, fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)


if __name__ == "__main__":
    c.run()



