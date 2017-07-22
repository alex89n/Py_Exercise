import os
from Tkinter import *      
root = Tk()

if os.path.isfile("list.txt"):
    os.remove("list.txt")
    

devices = []
def Click(event):
    devices = map((lambda var: var.get()), states)
    if os.path.isfile("list.txt"):
        os.remove("list.txt")
    for i in xrange(len(devices)):
        if devices[i] == 1:
            with open("list.txt", "a") as file:
                file.write(str(i+1) + ",True\n")
        if devices[i] == 0:
            with open("list.txt", "a") as file:
                file.write(str(i+1) + ",False\n")

def Unselect(event):
    for i in xrange(len(btn)):
        btn[i].toggle()
       
states = []
btn=[]
k=0
for i in xrange(5):
    for j in xrange(4):
        var = IntVar()
        btn.append(Checkbutton(root, text=str(k+1), variable=var))
        btn[k].grid(row = i, column = j, sticky = W)
        btn[k].select()
        states.append(var)
        k+=1

selc = Button(root, text = "Select All", state = ACTIVE)
selc.grid(row = 6, column = 0, columnspan = 2, padx = 11, pady = 5, sticky = W)
selc.bind("<Button-1>", Unselect)


submit = Button(root, text = "Continue")
submit.grid(row = 6, column = 2,  columnspan = 2, padx = 5, pady = 5, sticky = W)
submit.bind("<Button-1>", Click)

root.geometry("160x160")
root.mainloop()
