# # import wx

# # class Example(wx.Frame):
  
    # # def __init__(self, parent, title):
        # # super(Example, self).__init__(parent, title=title, size=(250, 200))            
        # # self.Centre()
        # # self.Show()


# # if __name__ == '__main__':
  
    # # app = wx.App()
    # # Example(None, title='Blah')
    # # app.MainLoop()
    

# import wx

# class Example(wx.Frame):
    
    # def __init__(self, *args, **kwargs):
        # super(Example, self).__init__(*args, **kwargs) 
            
        # self.InitUI()
        
    # def InitUI(self):    

        # menubar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        # menubar.Append(fileMenu, '&File')
        # self.SetMenuBar(menubar)
        
        # self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        # self.SetSize((300, 200))
        # self.SetTitle('Simple menu')
        # self.Centre()
        # self.Show(True)
        
    # def OnQuit(self, e):
        # self.Close()

# def main():
    
    # ex = wx.App()
    # Example(None)
    # ex.MainLoop()    


# if __name__ == '__main__':
    # main()
    
    #!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode wxPython tutorial

This example creates a checked
menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import os

dws_config_file = "d:\\_DWS_TestList"

global dugme

class Example(wx.Frame):
    global dugme 
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   

        pnl = wx.Panel(self)
        dugme = []
        wx.StaticBox(pnl, label='Chose DUT for testing', pos=(20, 10), size=(250, 300))
        cb = wx.CheckBox(pnl, label="DUT 1", pos=(30, 30))
        cb.SetValue(True)
        dugme.append(cb)
        cb = wx.CheckBox(pnl, label="DUT 2", pos=(90, 30))
        cb.SetValue(True)
        dugme.append(cb)
        cb = wx.CheckBox(pnl, label="DUT 3", pos=(150, 30))
        cb.SetValue(True)
        dugme.append(cb)
        cb = wx.CheckBox(pnl, label="DUT 4", pos=(210, 30))
        cb.SetValue(True)
        dugme.append(cb)
        
        
        # cb=[]
        # k=0
        # for i in xrange(5):
            # for j in xrange(4):
                # cb.append(wx.CheckBox(pnl, label=str(k+1), pos=((2*j+1)*30, i*30)))
                # cb[k].SetValue(True)
                # print cb[i].GetValue()
                # k+=1
        
        print len(dugme)
        print dugme[3].IsChecked()
        # var = IntVar()
                # btn.append(Checkbutton(root, text=str(k+1), variable=var))
                # btn[k].grid(row = i, column = j, sticky = W)
                # btn[k].select()
                # states.append(var)
        
        
        cbtn = wx.Button(pnl, label='Close', pos=(50, 250))
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
        
        cbtn = wx.Button(pnl, label='Continue', pos=(50, 280))
        cbtn.Bind(wx.EVT_BUTTON, self.Click)
        # cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
        
        
        dugme[3].Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)
        # print "is checked"
        # print cb[19].IsChecked()

        self.SetSize((400, 500))
        self.SetTitle('Devices')
        self.Centre()
        self.Show(True)



    def Click(self, e):
        for i in xrange(len(dugme)):
            if dugme[i].IsChecked() == True:
                with open(dws_config_file, "a") as file:
                    file.write(str(i+1) + ",True\n")
            if dugme[i].IsChecked() == False:
                with open(dws_config_file, "a") as file:
                    file.write(str(i+1) + ",False\n")

    def ShowOrHideTitle(self, e):        
        # sender = e.GetEventObject()
        isChecked = e.GetEventObject().GetValue()        
        if isChecked:
            self.SetTitle('wx.CheckBox')            
        else: 
            self.SetTitle('')
        print isChecked

    def OnClose(self, e):        
        self.Close(True)
                       
def main():
    if os.path.isfile(dws_config_file):
        os.remove(dws_config_file)
        
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()   