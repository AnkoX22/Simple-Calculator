import tkinter as tk
from tkinter import Frame
from tkinter import Button
from tkinter import Tk
from tkinter import Pack
from tkinter import Entry
from tkinter import DISABLED
from tkinter import BOTTOM

master = Tk()
master.geometry("300x400")
master.title("Simple Calculator")

buttonFrame = Frame(master)
buttonFrame.pack(side=BOTTOM)



displayFrame = Frame(master)
displayFrame.pack()

input = tk.StringVar()

# create constants for interface
h = 3
w = 5
px = 2
py = 2
num1=0
num2=0


#the display entry for the input
display = Entry(displayFrame,textvariable=input)
display.pack(ipady=3)

# command function of clear button
def clear():
    display.delete(0, tk.END)

# command function for c button
def c():
    display.delete(len(display.get())-1,len(display.get()))


# command function for ce button
def ce():
    lastNumeric = display.get()
    i = 1
    while lastNumeric[len(lastNumeric)-i].isnumeric():
        i +=1

    display.delete(len(display.get())-i+1,len(display.get()))



# command function for equal button
def equal():
    try:
        y = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for the 2nd power button
def power2():
    try:
        y = str(pow(float(display.get()),2))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for inverse function 
def inverse():
    try:
        y = str(1/float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for sqrt button
def sqrt():
    try:
        y = str(squareRoot(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for reverse button
def reverse():
    try:
        y = str(-float(display.get()))
        display.delete(0,tk.END)
        display.insert(0,y)
    except:
        display.insert(0,"Error")

# command function to insert in display the numbers of the pressed buttons
def onClick(name):
    display.insert(tk.END,name)

# create perCent button
perCent = Button(buttonFrame,text='%',height=h,width=w,command=lambda: onClick("%"))
perCent.grid(row=1,column=1,padx=px,pady=py) # insert perCent button in interface

#create ce button
ce = Button(buttonFrame,text='CE',height=h,width=w,command= ce)
ce.grid(row=1,column=2,padx=px,pady=py) # insert ce button in interface

# create c button
c = Button(buttonFrame,text='C',height=h,width=w,command= c)
c.grid(row=1,column=3,padx=px,pady=py) # insert c button in interface

# create delete button
delete = Button(buttonFrame,text='delete',height=h,width=w,command=clear) 
delete.grid(row=1,column=4,padx=px,pady=py) # insert delete button in interface

# create inverse button
inverse = Button(buttonFrame,text='1/x',height=h,width=w,command=inverse)
inverse.grid(row=2,column=1,padx=px,pady=py) # insert inverse button in interface

# create power2 button
power2 = Button(buttonFrame,text='^2',height=h,width=w,command=power2)
power2.grid(row=2,column=2,padx=px,pady=py) # insert power2 button in interface

#  create square root button
squareRoot = Button(buttonFrame,text='sqrt()',height=h,width=w,command=sqrt)
squareRoot.grid(row=2,column=3,padx=px,pady=py) # insert square root button in interface

# create division button
division = Button(buttonFrame,text='/',height=h,width=w,command=lambda: onClick("/"))
division.grid(row=2,column=4,padx=px,pady=py) # insert division button in interface

# create the 7(number) button
b7 = Button(buttonFrame,text='7',height=h,width=w,command=lambda: onClick("7"))
b7.grid(row=3,column=1,padx=px,pady=py) # insert button 7 in interface

# create button 8(number)
b8 = Button(buttonFrame,text='8',height=h,width=w,command=lambda: onClick("8"))
b8.grid(row=3,column=2,padx=px,pady=py) # insert button 8 in interface

# create button 9(number)
b9 = Button(buttonFrame,text='9',height=h,width=w,command=lambda: onClick("9"))
b9.grid(row=3,column=3,padx=px,pady=py) # insert button 9 in interface

# create multiplication button
multip = Button(buttonFrame,text='*',height=h,width=w,command=lambda: onClick("*"))
multip.grid(row=3,column=4,padx=px,pady=py) # insert multiplication button in interface

# create button 4 (number)
b4 = Button(buttonFrame,text='4',height=h,width=w,command=lambda: onClick("4"))
b4.grid(row=4,column=1,padx=px,pady=py) # insert four button in interface

# create button 5 (number)
b5 = Button(buttonFrame,text='5',height=h,width=w,command=lambda: onClick("5"))
b5.grid(row=4,column=2,padx=px,pady=py) # insert button five in interface

# create button 6 (number)
b6 = Button(buttonFrame,text='6',height=h,width=w,command=lambda: onClick("6"))
b6.grid(row=4,column=3,padx=px,pady=py) # insert button six in interface

# create minus button
minus = Button(buttonFrame,text='-',height=h,width=w,command=lambda: onClick("-"))
minus.grid(row=4,column=4,padx=px,pady=py) # insert minus button in interface

# create button 1 (number)
b1 = Button(buttonFrame,text='1',height=h,width=w,command=lambda: onClick("1"))
b1.grid(row=5,column=1,padx=px,pady=py) # insert button one in interface

# create button 2 (number)
b2 = Button(buttonFrame,text='2',height=h,width=w,command=lambda: onClick("2"))
b2.grid(row=5,column=2,padx=px,pady=py) # insert button 2 in interface

# create button 3 (number)
b3 = Button(buttonFrame,text='3',height=h,width=w,command=lambda: onClick("3"))
b3.grid(row=5,column=3,padx=px,pady=py) # insert button 3 in interface

# create plus button
plus = Button(buttonFrame,text='+',height=h,width=w,command=lambda: onClick("+"))
plus.grid(row=5,column=4,padx=px,pady=py) # insert plus button in interface

# create reverse button
reverse = Button(buttonFrame,text='+/-',height=h,width=w,command=reverse)
reverse.grid(row=6,column=1,padx=px,pady=py) # insert reverse button in interface

# create  button 0 (number)
b0 = Button(buttonFrame,text='0',height=h,width=w,command=lambda: onClick("0"))
b0.grid(row=6,column=2,padx=px,pady=py) # insert zero button in interface

# create dot button
dot = Button(buttonFrame,text='.',height=h,width=w,command=lambda: onClick("."))
dot.grid(row=6,column=3,padx=px,pady=py) # insert dot button in interface

# create equal button
equal = Button(buttonFrame,text='=',height=h,width=w,command=equal)
equal.grid(row=6,column=4,padx=px,pady=py) # insert equal button in interface

# run interface
master.mainloop()
