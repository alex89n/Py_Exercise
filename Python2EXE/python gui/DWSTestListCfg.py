import os
from Tkinter import *      
root = Tk()

# dws_config_file = "d:\\_DWS_TestList"
dws_config_file = "d:\\_BSC_TestList"

# if os.path.isfile(dws_config_file):
    # os.remove(dws_config_file)
    

devices = []
def Click(event):
    devices = map((lambda var: var.get()), states)
    if os.path.isfile(dws_config_file):
        os.remove(dws_config_file)
    for i in xrange(len(devices)):
        if devices[i] == 1:
            with open(dws_config_file, "a") as file:
                file.write(str(i+1) + ",True\n")
        if devices[i] == 0:
            with open(dws_config_file, "a") as file:
                file.write(str(i+1) + ",False\n")

def Unselect(event):
    for i in xrange(len(btn)):
        btn[i].toggle()
        
def close(): 
    root.destroy()
       
states = []
btn=[]
k=0
for i in xrange(4):
    for j in xrange(4):
        var = IntVar()
        btn.append(Checkbutton(root, text=str(k+1), variable=var))
        btn[k].grid(row = i+2, column = j+2, sticky = (W))
        btn[k].select()
        states.append(var)
        k+=1

selc = Button(root, text = "Select All", state = ACTIVE)
selc.grid(row = 8, column = 2, columnspan = 2, padx = 11, pady = 5, sticky = (W, S))
selc.bind("<Button-1>", Unselect)


submit = Button(root, text = "Continue", command = close)
submit.grid(row = 8, column = 4,  columnspan = 2, padx = 5, pady = 5, sticky = (W, S))
submit.bind("<Button-1>", Click)
submit.focus()

lab = Label(root, text="       ").grid(row=0, column = 0, sticky=W)
lab = Label(root, text=" ").grid(row=6, column = 0, sticky=W)
lab = Label(root, text=" ").grid(row=7, column = 0, sticky=W)



def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinatess
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
center_window(220, 210)
root.title("Select DUT to test")
# root.iconbitmap('A.ico')
root.mainloop()
