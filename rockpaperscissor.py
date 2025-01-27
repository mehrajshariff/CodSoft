import tkinter as tk
import random

user_score=0
computer_score=0
ties=0

def play(user_choice):
    global user_score, computer_score, ties
    choices=["Rock","Paper","Scissors"]
    computer_choice=random.choice(choices)
    if user_choice == computer_choice:
        result="It's a tie!"
        ties +=1
    elif(
        (user_choice=="Rock" and computer_choice == "Scissors")or
        (user_choice=="Scissors" and computer_choice == "Rock")or
        (user_choice=="Paper" and computer_choice == "Rock") 
    ):
        result="You win!"
        user_score +=1
    else:
        result="You Lose!"
        computer_score +=1
        
    result_label.config(text=f"You: {user_choice}\nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        
root=tk.Tk()
root.title("Rock-Paper-Scissors")

result_label=tk.Label(root,text="Choose Rock,Paper, Or Scissors",font=("Arial",14))
result_label.pack(pady=20)        

buttons_frame=tk.Frame(root)
buttons_frame.pack()

for choice in["Rock","Paper","Scissors"]:
    button=tk.Button(buttons_frame,text=choice,font=("Arial",12),command=lambda c=choice:play(c))
    button.pack(side=tk.LEFT,padx=10,pady=10)
    
score_label=tk.Label(root,text="Score-You:0 | Computer:0 | Ties:0",font=("Arial",12))
score_label.pack(pady=20)

root.mainloop()    
            
     
        