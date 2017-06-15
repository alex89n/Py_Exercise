from Tkinter import *

root = Tk()
var = []
def leftClick(event):
    print "Left Click"
def rightClick(event):
    print "Right Click"
    print var.get()

def makeDoc(state):
    with open("_DWS_list","w") as file:
        for i in xrange(16):
            file.write(str(i) + "," + state + "\n")
            
def createButton(cbox, name = "1", row = 0, column = 0):
    cbox = Checkbutton(root, text = name, variable = var)
    cbox.grid(row = row, column = column, sticky = W)
    return cbox

# create all buttons 4x4
btn=[]
k=1
for i in range(4):
    for j in xrange(4):
        var = IntVar()
        btn.append(createButton("b"+str(k), k, i, j))
        k+=1


btn[0].bind("<Button-1>", leftClick)
btn[1].bind("<Button-3>", rightClick)
btn[2].bind("<Button-1>", leftClick)
btn[11].bind("<Button-1>", rightClick)

##print var.get()
##cbox = Checkbutton(root, text = "DUT 1")
##cbox.grid(sticky = E, row = 0, column = 0)
##cbox = Checkbutton(root, text = "DUT 2")
##cbox.grid(row = 0, column = 1)
##cbox = Checkbutton(root, text = "DUT 3")
##cbox.grid(row = 0, column = 2)
##cbox = Checkbutton(root, text = "DUT 4")
##cbox.grid(row = 0, column = 3)
##
##cbox = Checkbutton(root, text = "DUT 5")
##cbox.grid(sticky = E, row = 1, column = 0)
##cbox = Checkbutton(root, text = "DUT 6")
##cbox.grid(row = 1, column = 1)
##cbox = Checkbutton(root, text = "DUT 7")
##cbox.grid(row = 1, column = 2)
##cbox = Checkbutton(root, text = "DUT 8")
##cbox.grid(row = 1, column = 3)
##
##cbox = Checkbutton(root, text = "DUT 9")
##cbox.grid(sticky = N, row = 2, column = 0)
##cbox = Checkbutton(root, text = "DUT 10")
##cbox.grid(row = 2, column = 1)
##cbox = Checkbutton(root, text = "DUT 11")
##cbox.grid(row = 2, column = 2)
##cbox = Checkbutton(root, text = "DUT 12")
##cbox.grid(row = 2, column = 3)
##
##cbox = Checkbutton(root, text = "DUT 13")
##cbox.grid(sticky = N, row = 3, column = 0)
##cbox = Checkbutton(root, text = "DUT 14")
##cbox.grid(row = 3, column = 1)
##cbox = Checkbutton(root, text = "DUT 15")
##cbox.grid(row = 3, column = 2)
##cbox = Checkbutton(root, text = "DUT 16")
##cbox.grid(row = 3, column = 3)


cbox = Checkbutton(root, text = "Select All")
cbox.grid(column = 0, columnspan = 2 , sticky = W)
cbox.bind("<Button-1>", cb)

submit = Button(root, text = "Continue")
submit.grid( column = 2, sticky = W)

root.geometry("200x200")
root.mainloop()
