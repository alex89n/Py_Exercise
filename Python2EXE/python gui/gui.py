from Tkinter import *

root = Tk()
##buttons
#topFrame = Frame(root)
#topFrame.pack()

#botFrame = Frame(root)
#botFrame.pack(side=BOTTOM)

##Button1 = Button(None, text = "Click Me", fg = "Blue", bg = "Yellow")
##Button1.pack()
##
##Button2 = Button(None, text = "Click Me", fg = "red")
##Button2.pack(fill = X)
##
##Button3 = Button(None, text = "Hello", fg = "Purple")
##Button3.pack(side=RIGHT, fill = Y)
##
##Button4 = Button(None, text = "Hello", fg = "Yellow")
##Button4.pack()

##labels

##label1 = Label(root, text = "Label 1")
##label2 = Label(root, text = "Label 2")
##label3 = Label(root, text = "Label 3")
##
##label1.grid(row = 0, column = 0)
##label2.grid(row = 0, column = 1)
##label3.grid(row = 1, column = 0)


##entries and check box
####label1 = Label(root, text = "Name:")
####label1.grid(row = 0, column = 0, sticky = E)
####
####label2 = Label(root, text = "Password:")
####label2.grid(row = 1, column = 0, sticky = E)
####
####entrySpace = Entry(root)
####entrySpace.grid(row = 0, column = 1)
####
####entrySpace2 = Entry(root)
####entrySpace2.grid(row = 1, column = 1)
####
####cbutton = Checkbutton(root, text = "Remember name")
####cbutton.grid(columnspan = 2)


##Actions
##def leftClick(event):
##    print "Left Click"
##    
##def rightClick(event):
##    print "Right Click"
##    
##def scroll(event):
##    print "Scroll"
##
##def leftKey(event):
##    print "Left Key Pressed"
##
##def rightKey(event):
##    print "Right Key Pressed"
    
##button1 = Button(root, text = "Click Me")
##button1.bind("<Button-1>", printName)
##button1.grid()

##cbutton = Checkbutton(root, text = "Remember name")
##cbutton.grid()
##cbutton.bind("<Button-1>", leftClick)
##
##
####root.bind("<Button-1>", leftClick)
##root.bind("<Button-3>", rightClick)
##root.bind("<Button-2>", scroll)
##root.bind("<Left>", leftKey)
##root.bind("<Right>", rightKey)

#get data from entries

def evaluate(event):
    data = e.get()
    ans.configure(text = "Answer: " + str(eval(data)))

label1 = Label(root, text = "Unestite izraz:")
label1.pack()
e = Entry(root)
e.pack()
e.bind("<Return>", evaluate)

ans = Label(root)
ans.pack()


##root.geometry("250x150")
root.mainloop()















