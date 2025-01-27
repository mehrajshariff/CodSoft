import tkinter as tk
import random
import string

def generate_password():
    try:
        length=int(entry_length.get())
        if length<=0:
            raise ValueError("length must be greater than 0")
        characters=string.ascii_letters+string.digits+string.punctuation 
        password="".join(random.choice(characters)for _ in range(length))
        result_label.config(text=f"Password:{password}")
    except ValueError as e:
        result_label.config(text=f"Error:{e}")
       
root=tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

tk.Label(root,text="Enter Password Length:").pack(pady=10)
entry_length=tk.Entry(root)
entry_length.pack(pady=5)

tk.Button(root,text="Generate Password",command=generate_password).pack(pady=10) 
result_label=tk.Label(root,text="")
result_label.pack(pady=10)

root.mainloop()      
        
               
        