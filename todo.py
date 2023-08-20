from tkinter import *
from tkinter import messagebox
root = Tk()

def adding_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(END, task)
        task_entry.delete(0,END)
    else:
        messagebox.showwarning("Warning", "Please enter a task to add.")

def removing_task():
    selected_task_remove = tasks_listbox.curselection()
    if selected_task_remove:
        tasks_listbox.delete(selected_task_remove)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root.title("To-Do List")

task_entry = Entry(root,width=60,border=15)
add_button = Button(root, text="Add Task",padx=10,pady=10,border=10,fg='black',font='bold 13', command=adding_task)
remove_button = Button(root, text="Remove Task",padx=10,pady=10,border=10,font='bold 13', command=removing_task)
tasks_listbox = Listbox(root,width=45,border=20)
task_entry.grid(row=0, column=0)

add_button.grid(row=0, column=1)
remove_button.grid(row=1, column=0, columnspan=2)
tasks_listbox.grid(row=2, column=0, columnspan=2)
tasks_listbox.configure(background="light yellow",foreground="blue",font=('Bold 15'))
root.mainloop()