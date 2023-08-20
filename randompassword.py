import random
import string
from tkinter import *

root=Tk()
root.title("Rando password")

no_of_passwords=Label(root,text="How many passwords do you want?")
no_of_passwords.pack()
passwords=Entry(root,width=35,bd=10)
passwords.pack()

password_length=Label(root,text="Enter length of password")
password_length.pack()
len=Entry(root,width=35,bd=10)
len.pack()

exitButton=Button(root,text='Exit program',padx=10,pady=20,border=10,command=root.destroy)
exitButton.pack()

def suggested_password():
    character=string.punctuation+string.ascii_letters+string.digits
    passwords_int=int(passwords.get())
    len_int=int(len.get())
    label1=Label(root,text="**********************************************************")
    label1.pack()
    for i in range(passwords_int):
        password=''
        for j in range(len_int):
            if(random.choice != string.whitespace):
                password+=random.choice(character)
        label2=Label(root,text=password,padx=100,pady=20,font="Helvetica 20 bold italic",fg="red")
        label2.pack()

def basic_password():
    character=string.ascii_letters+string.digits
    passwords_int=int(passwords.get())
    len_int=int(len.get())
    label1=Label(root,text="****************************************")
    label1.pack()
    for i in range(passwords_int):
        password=''
        for j in range(len_int):
            if(random.choice != string.whitespace):
                password+=random.choice(character)
        label3=Label(root,text=password,padx=100,pady=20,font="Helvetica 20 bold italic",fg="red")
        label3.pack()

complex_button=Button(root,text="complex passwords",padx=10,pady=20,border=10,command=suggested_password)
basic_button=Button(root,text="basic passwords",padx=10,pady=20,border=10,command=basic_password)
complex_button.pack()
basic_button.pack()

root.mainloop()