import Tkinter
import os
import sys
app = Tkinter.Tk()

def startTips():
    os.chdir('html')
    os.startfile('home.html')
    os.chdir('..')
    sys.exit()

Txt = Tkinter.Label(app, text="Hello!", font = (20))
Txt.pack()
Txt = Tkinter.Label(app, text="It seems that you are new!", font = (5))
Txt.pack()
start = Tkinter.Button(app, text = 'here are some tips to get you started!', width = 60, command = startTips)
start.pack(padx = 15, pady = 15)

app.mainloop()
