import tkinter as tk

def press(key):
    current=equation.get()
    equation.set(current+str(key))
    
def calculate():
    try:
        result=str(eval(equation.get()))
        equation.set(result) 
    except:
        equation.set("Error")
        
def clear():
    equation.set("")
    
root=tk.Tk()
root.title("calculator")
root.geometry("300x400") 

equation=tk.StringVar()
entry=tk.Entry(root,textvariable=equation,font=("Arial",20),bd=10,insertwidth=2,width=14,borderwidth=4,justify="right")
entry.grid(row=0,column=0,columnspan=4)

buttons=[
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('C',4,0),('0',4,1),('=',4,2),('+',4,3),
]

for(text,row,col)in buttons:
    if text == '=':
        button=tk.Button(root,text=text,padx=20,pady=20,font=("Arial",15),command=calculate)
    elif text =='C':    
        button=tk.Button(root,text=text,padx=20,pady=20,font=("Arial",15),command=clear) 
                         
    else:
        button=tk.Button(root,text=text,padx=20,pady=20,font=("Arial",15),command=lambda t=text:press(t))
        
    button.grid(row=row, column=col)

root.mainloop()        
            