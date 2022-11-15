from tkinter import *
t=Tk()
t.overrideredirect(1)


t.config(bg="black")

t.title((" "*80)+"Sliding puzzle")
t.resizable()
f=Frame(t,bg="#000")
f.place(x=0,y=0,width=600,height=600)
lf=[]
lt=[]
ltc=[]
Lab=[]
cmp=0
from PIL import Image,ImageTk
path="y.png"
for i in range(3):
    for j in range(3):
        lf.append(Frame(f))
        if i==2 and j==2:
            Lab.append(Label(lf[cmp],background="#242424"))
            lt.append(["",cmp])
            ltc.append(["",cmp])
        else:
            lt.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp])
            ltc.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp])
            Lab.append(Label(lf[cmp],image=lt[cmp][0],background="#3b53a0"))
        Lab[cmp].bind("<Button-1>",lambda event,h=cmp:play(event,h))
        Lab[cmp].place(x=2,y=2,width=196,height=196)
        lf[cmp].place(x=j*200,y=i*200,width=200,height=200)
        cmp+=1
index=8
from threading import Thread
def play(event,h):
    global index,t
    if Lab[h].cget("bg")=="#242424" and (h-1==index or h+1==index or h+3==index or h-3==index) :
        Lab[h].config(image=ltc[index][0])
        ih=ltc[h][1]
        ltc[h]=[ltc[index][0],ltc[index][1]]
        ltc[index]=["",ih]
        Lab[index].config(image="")
        Lab[h].config(bg="#3b53a0")
        Lab[index].config(bg="#242424")
        k=0
        for i in range(len(ltc)):
            if ltc[i][1]==lt[i][1]:
                k+=1
        if k==(len(ltc)):
            changetheimage.place_forget()
            youwin.place(x=0,y=600,width=600,height=50)
            b=False
            Thread(target=lambda y=youwin:tim(y)).start()
    lf[index].config(bg="white")
    index=h
    lf[h].config(bg="black")
yw=ImageTk.PhotoImage((Image.open("button.png")))
yww=ImageTk.PhotoImage((Image.open("button.png")))
youwin=Label(t,image=yw)
from time import sleep

iim=ImageTk.PhotoImage((Image.open("button.png")))
iimw=ImageTk.PhotoImage((Image.open("button.png")))
restart=Label(t,image=iim)
restart.place(x=600,y=0,width=50,height=600)
restart.bind("<Enter>",lambda event:restart.config(image=iimw))
restart.bind("<Leave>",lambda event:restart.config(image=iim))
_a89=ImageTk.PhotoImage((Image.open("button.png")))
a89=Label(t,image=_a89)
a89.place(x=600,y=600,width=50,height=50)
from tkinter import messagebox
from tkinter import filedialog
cti=ImageTk.PhotoImage((Image.open("button.png")))
ctiw=ImageTk.PhotoImage((Image.open("button.png")))
changetheimage=Label(t,image=cti)
changetheimage.place(x=0,y=600,width=600,height=50)
changetheimage.bind("<Enter>",lambda event:changetheimage.config(image=ctiw))
changetheimage.bind("<Leave>",lambda event:changetheimage.config(image=cti))

from random import shuffle
b=False

def reimage(event):
    global ltc,Lab,b
    if event:
        shuffle(ltc)
    for i in range(len(ltc)):
        Lab[i].config(image=ltc[i][0])
        Lab[i].config(bg="#3b53a0")
    for j in range(len(ltc)):
        if ltc[j][0]=="":
            Lab[j].config(bg="#242424")
    b=True
    youwin.place_forget()
    changetheimage.place(x=0,y=600,width=600,height=50)
restart.bind("<Button-1>",reimage)

introf=Frame(t)
introf.place(x=0,y=0,width=650,height=650)

introi=[ImageTk.PhotoImage(Image.open("button.png").resize((300,300))),ImageTk.PhotoImage(Image.open("button.png").resize((300,300))),ImageTk.PhotoImage(Image.open("button.png").resize((300,300)))]
introl=Label(introf,bg="#3b53a0")
introl.place(x=0,y=0,width=650,height=650)
def intro():
    icmp=0
    ic=0

    while True:
        introl.config(image=introi[icmp])
        sleep(0.2)
        ic+=1
        icmp+=1
        if icmp==3:
            icmp=0
        if ic==9:
            break
    introf.place_forget()
    t.geometry(f"650x650")
    t.overrideredirect(0)
t.after(1,lambda :Thread(target=intro).start())
t.mainloop()