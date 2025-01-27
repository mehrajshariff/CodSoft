import tkinter as tk
from tkinter import messagebox
contacts={}
def add_contact():
    name=entry_name.get()
    phone=entry_phone.get()
    email=entry_email.get()
    address=entry_address.get()
    if name and phone:
        contacts[name]={'Phone':phone,'Email':email,'Address':address}
        entry_name.delete(0,tk.END)
        entry_phone.delete(0,tk.END)
        entry_email.delete(0,tk.END) 
        entry_address.delete(0,tk.END)
        display_contacts()
    else:
        messagebox.showwarning("Warning","Name and Phone arerequired!")
def display_contacts():
    listbox_contacts.delete(0,tk.END)
    for name,details in contacts.items():
         listbox_contacts.insert(tk.END,f"{name}-{details['Phone']}")

def search_contact():
    query=entry_search.get()
    listbox_contacts.delete(0,tk.END)  
    for name,details in contacts.items():
         if query.lower() in name.lower() or query in details['Phone']:
              listbox_contacts.insert(tk.END,f"{name}-{details['Phone']}")
              
def update_contact():
    try:
        selected=listbox_contacts.get(listbox_contacts.curselection())
        name=selected.split('-')[0]
        if name in contacts:
            contacts[name]={
                'Phone':entry_phone.get(),
                'Email':entry_email.get(),
                'Address':entry_address.get()
                }
            display_contacts()
    except IndexError:
        messagebox.showwarning("Warning","No contact selected!")

def delete_contact():
    try:
        selected=listbox_contacts.get(listbox_contacts.curselection())
        name=selected.split('-')[0]
        if name in contacts:
            del contacts[name]
            display_contacts()
    except IndexError:
        messagebox.showwarning("Warning","No contact selected!")
        
root=tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")

tk.Label(root,text="Name:").pack()
entry_name=tk.Entry(root)
entry_name.pack()

tk.Label(root,text="Phone:").pack()
entry_phone=tk.Entry(root)
entry_phone.pack()

tk.Label(root,text="Email:").pack()
entry_email=tk.Entry(root)
entry_email.pack()

tk.Label(root,text="Address:").pack()
entry_address=tk.Entry(root)
entry_address.pack()

tk.Button(root,text="Add Contact",
          command=add_contact).pack(pady=5)
tk.Label(root,text="Search:").pack()
entry_search=tk.Entry(root)
entry_search.pack()
tk.Button(root,text="Search",
          command=search_contact).pack(pady=5)

tk.Button(root,text="Update Contact",
          command=update_contact).pack(pady=5)
tk.Button(root,text="Delete Contact",
          command=delete_contact).pack(pady=5)

tk.Label(root,text="Contact List:").pack()
listbox_contacts=tk.Listbox(root,width=50,height=15)
listbox_contacts.pack(pady=10)

root.mainloop()
                                
            
                   
        
    