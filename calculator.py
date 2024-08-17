from tkinter import *
from tkinter import ttk
import math

master = Tk()
master.geometry("350x220")
master.title("Simple Calculator")

buttonFrame = Frame(master)
buttonFrame.pack(side=BOTTOM)



displayFrame = Frame(master)
displayFrame.pack()

input = StringVar()

# create constants for interface
h = 3
w = 5
px = 2
py = 2
num1=0
num2=0


#the display entry for the input
display = ttk.Entry(displayFrame,textvariable=input)
display.pack(ipady=3)

# command function of clear button
def clear():
    display.delete(0, END)

# command function for c button
def c():
    display.delete(len(display.get())-1,len(display.get()))


# command function for ce button
def ce():
    lastNumeric = display.get()
    try:
        i = 1
        while lastNumeric[len(lastNumeric)-i].isnumeric():
            i +=1

        display.delete(len(display.get())-i+1,len(display.get()))
    except:
        display.delete(0,END)


# command function for equal button
def equal():
    try:
        y = str(eval(display.get()))
        display.delete(0, END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for the 2nd power button
def power2():
    try:
        y = str(pow(float(display.get()),2))
        display.delete(0, END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for inverse function 
def inverse():
    try:
        y = str(1/float(display.get()))
        display.delete(0, END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for sqrt button
def sqroot():
    input = float(display.get())
    try:
        y = str(math.sqrt(input))
        display.delete(0, END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

# command function for reverse button
def reverse():
    try:
        y = str(-float(display.get()))
        display.delete(0,END)
        display.insert(0,y)
    except:
        display.insert(0,"Error")

# command function to insert in display the numbers of the pressed buttons
def onClick(name):
    display.insert(END,name)

# create perCent button
perCent = ttk.Button(buttonFrame,text='%',command=lambda: onClick("%"))
perCent.grid(row=1,column=1,padx=px,pady=py) # insert perCent button in interface

#create ce button
ce = ttk.Button(buttonFrame,text='CE',command= ce)
ce.grid(row=1,column=2,padx=px,pady=py) # insert ce button in interface

# create c button
c = ttk.Button(buttonFrame,text='C',command= c)
c.grid(row=1,column=3,padx=px,pady=py) # insert c button in interface

# create delete button
delete = ttk.Button(buttonFrame,text='delete',command=clear) 
delete.grid(row=1,column=4,padx=px,pady=py) # insert delete button in interface

# create inverse button
inverse = ttk.Button(buttonFrame,text='1/x',command=inverse)
inverse.grid(row=2,column=1,padx=px,pady=py) # insert inverse button in interface

# create power2 button
power2 = ttk.Button(buttonFrame,text='^2',command=power2)
power2.grid(row=2,column=2,padx=px,pady=py) # insert power2 button in interface

#  create square root button
squareRoot = ttk.Button(buttonFrame,text='sqrt()',command=sqroot)
squareRoot.grid(row=2,column=3,padx=px,pady=py) # insert square root button in interface

# create division button
division = ttk.Button(buttonFrame,text='/',command=lambda: onClick("/"))
division.grid(row=2,column=4,padx=px,pady=py) # insert division button in interface

# create the 7(number) button
b7 = ttk.Button(buttonFrame,text='7',command=lambda: onClick("7"))
b7.grid(row=3,column=1,padx=px,pady=py) # insert button 7 in interface

# create button 8(number)
b8 = ttk.Button(buttonFrame,text='8',command=lambda: onClick("8"))
b8.grid(row=3,column=2,padx=px,pady=py) # insert button 8 in interface

# create button 9(number)
b9 = ttk.Button(buttonFrame,text='9',command=lambda: onClick("9"))
b9.grid(row=3,column=3,padx=px,pady=py) # insert button 9 in interface

# create multiplication button
multip = ttk.Button(buttonFrame,text='*',command=lambda: onClick("*"))
multip.grid(row=3,column=4,padx=px,pady=py) # insert multiplication button in interface

# create button 4 (number)
b4 = ttk.Button(buttonFrame,text='4',command=lambda: onClick("4"))
b4.grid(row=4,column=1,padx=px,pady=py) # insert four button in interface

# create button 5 (number)
b5 = ttk.Button(buttonFrame,text='5',command=lambda: onClick("5"))
b5.grid(row=4,column=2,padx=px,pady=py) # insert button five in interface

# create button 6 (number)
b6 = ttk.Button(buttonFrame,text='6',command=lambda: onClick("6"))
b6.grid(row=4,column=3,padx=px,pady=py) # insert button six in interface

# create minus button
minus = ttk.Button(buttonFrame,text='-',command=lambda: onClick("-"))
minus.grid(row=4,column=4,padx=px,pady=py) # insert minus button in interface

# create button 1 (number)
b1 = ttk.Button(buttonFrame,text='1',command=lambda: onClick("1"))
b1.grid(row=5,column=1,padx=px,pady=py) # insert button one in interface

# create button 2 (number)
b2 = ttk.Button(buttonFrame,text='2',command=lambda: onClick("2"))
b2.grid(row=5,column=2,padx=px,pady=py) # insert button 2 in interface

# create button 3 (number)
b3 = ttk.Button(buttonFrame,text='3',command=lambda: onClick("3"))
b3.grid(row=5,column=3,padx=px,pady=py) # insert button 3 in interface

# create plus button
plus = ttk.Button(buttonFrame,text='+',command=lambda: onClick("+"))
plus.grid(row=5,column=4,padx=px,pady=py) # insert plus button in interface

# create reverse button
reverse = ttk.Button(buttonFrame,text='+/-',command=reverse)
reverse.grid(row=6,column=1,padx=px,pady=py) # insert reverse button in interface

# create  button 0 (number)
b0 = ttk.Button(buttonFrame,text='0',command=lambda: onClick("0"))
b0.grid(row=6,column=2,padx=px,pady=py) # insert zero button in interface

# create dot button
dot = ttk.Button(buttonFrame,text='.',command=lambda: onClick("."))
dot.grid(row=6,column=3,padx=px,pady=py) # insert dot button in interface

# create equal button
equal = ttk.Button(buttonFrame,text='=',command=equal)
equal.grid(row=6,column=4,padx=px,pady=py) # insert equal button in interface

# run interface
master.mainloop()
