print("Hello World")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root,
                text="らべるを書いてみた件",
                font=("Ricty Diminished", 40)
                )
label.pack()

button = tk.Button(root, text="押すな" ,font=("",30))
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()



root.mainloop()
