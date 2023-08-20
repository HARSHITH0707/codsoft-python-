from tkinter import *
root=Tk()
root.title("calculator")
num1=Label(root,text="Enter first Number ")
num1.pack()
entry1=Entry(root,width=35,bd=10)
num2=Label(root,text="Enter second Number ")
entry2=Entry(root,width=35,bd=10)
entry1.pack()
num2.pack()
entry2.pack()
def add():
    a=float(entry1.get())
    b=float(entry2.get())
    c=a+b
    display.insert(END,c)
def sub():
    a=float(entry1.get())
    b=float(entry2.get())
    c=a-b
    display.insert(END,c)
def multiply():
    a=float(entry1.get())
    b=float(entry2.get())
    c=a*b
    display.insert(END,c)
def divide():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a/b
    display.insert(END,c)
display=Listbox(root,width=35,border=10)
display.configure(bg='light green',fg='blue',font='bold 12')
display.pack()
msg1=Button(root,text="+",padx=30,pady=25,border=5,command=add)
msg2=Button(root,text="-",padx=30,pady=25,border=5,command=sub)
msg3=Button(root,text="*",padx=30,pady=25,border=5,command=multiply)
msg4=Button(root,text="%",padx=30,pady=25,border=5,command=divide)
msg1.pack(side=LEFT)
msg2.pack(side=LEFT)
msg3.pack(side=RIGHT)
msg4.pack(side=RIGHT)
root.mainloop()
