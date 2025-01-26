import tkinter as tk
from tkinter import messagebox

def add_task():
    task=entry_task.get()
    if task:
        listbox_tasks.insert(tk.END,task)
        entry_task.delete(0,tk.END)
    else:
      messagebox.showwarning("warning","Task cannot be empty!") 
      
def remove_task():
    try:
        selected_task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("warning","no task selected!")

def mark_done():
    try:
        selected_task_index=listbox_tasks.curselection()[0]
        task=listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END,f"[Done]{task}")
    except IndexError:
        messagebox.showwarning("warning","no task selected!")

def exit_app():
    root.destroy()
    
root=tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

tk.Label(root,text="To-Do List",font=("Helvetica",16)).pack(pady=10) 
frame_tasks=tk.Frame(root)     
frame_tasks.pack(pady=10)

listbox_tasks=tk.Listbox(frame_tasks,width=40,height=15)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks=tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT,fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task=tk.Entry(root,width=30)
entry_task.pack(pady=5)

tk.Button(root,text="ADD TASK",command=add_task).pack(pady=5)
tk.Button(root,text="REMOVE TASK",command=remove_task).pack(pady=5)
tk.Button(root,text="TASK DONE",command=mark_done).pack(pady=5)
tk.Button(root,text="EXIT",command=exit_app).pack(pady=5)

root.mainloop()
   
                
                 