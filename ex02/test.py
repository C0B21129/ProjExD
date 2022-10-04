print("seijou")

import tkinter as tk
import tkinter.messagebox as tkm

root =tk.Tk()
root.geometry("300x700")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    justify.insert(tk.END,f"{txt}")

def button_e_click(event_e):
    eqn = justify.get()
    if eqn=="893++":
        yakuza()
    elif eqn=="+-*/":
        fever()
    res = eval(eqn)
    justify.delete(0, tk.END)
    justify.insert(tk.END, res) 

def button_e_click_l(event_e_l):
    justify.delete(0, tk.END)

def yakuza():
    justify.delete(0, tk.END)
    justify.insert(tk.END, "しばくぞ！")
    
def fever():
    justify.delete(0, tk.END)
    justify.insert(tk.END, "fever")
    root2 =tk.Tk()
    root2.title("fv")
    root2.geometry("5000x4000")
    label = tk.Label(root,
                    text="FEVER",
                    font=("Ricty Diminished", 100)
                    )
    label.pack()
c=0
r=1


for i in range(9,-5,-1):
    if i==-1:
        i="+"
    elif i==-2:
        i="-"
    elif i==-3:
        i="*"
    elif i==-4:
        i="/"
    button = tk.Button(root, text=i,font=("Times New Roman",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c+=1
    if c==3:
        r+=1
        c=0
    
button_e = tk.Button(root, text="=",font=("Times New Roman",30),width=4,height=2)
button_e.bind("<1>",button_e_click)
button_e.bind("<3>",button_e_click_l)
button_e.grid(row=r,column=c)
    
justify = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
justify.grid(row=0,column=0,columnspan=3)
    
root.mainloop()