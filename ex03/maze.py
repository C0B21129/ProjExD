import tkinter as tk
import maze_maker as mm
import time

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,my,mx
    
    if key=="Up":
        my-=1
    if key=="Down":
        my+=1
    if key=="Right":
        mx+=1
    if key=="Left":
        mx-=1
    if maze_lst[my][mx]==0:
        cx,cy=mx*100+50,my*100+50
    if maze_lst[my][mx]==1:
        if key=="Up":
            my+=1
        if key=="Down":
            my-=1
        if key=="Right":
            mx-=1
        if key=="Left":
            mx+=1
    if maze_lst[my][mx]==2:
        cx,cy=mx*100+50,my*100+50
        canv.create_text(750,450,text="Congratulation!!",font=("Ricty Diminished", 150),fill="blue")
        hora= tk.PhotoImage(file = "ex03/hora.png")
        time.sleep(3000,canv.create_image(750,450,image=hora,tag="hora"))
        
        root.mainloop()

    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

#1
root=tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")

#2
canv=tk.Canvas(root,width=1500,height=900,bg="black")
canv.pack()

#9,10
maze_lst = mm.make_maze(15,9)
print(maze_lst)#1壁/0道
mm.show_maze(canv,maze_lst)

#3
tori = tk.PhotoImage(file = "ex03/fig/3.png")
mx,my = 1,1
cx,cy=mx*100+50,my*100+50
canv.create_image(cx+50,cy+50,image=tori,tag="tori")

#4
key=""

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

main_proc()

root.mainloop()