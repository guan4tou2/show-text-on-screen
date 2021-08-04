import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.title("panel")


win.geometry('200x100+%d+%d'%(win.winfo_screenwidth()/2-100,win.winfo_screenheight()/2-100))
showwin=tk.Toplevel(win)
showwin.geometry("+0+0")
showwin.state('icon')
entry=tk.Entry(win)
tex=tk.StringVar()
label = tk.Label(showwin,textvariable=tex,font=("Fira Code",40)).pack()
def settext():
    showwin.state('normal')
    showwin.attributes("-toolwindow",1)
    showwin.attributes("-topmost",1)
    showwin.attributes("-alpha",0.7)
    showwin.overrideredirect(True)
    tex.set(entry.get())

def setgeometry():
    showwin.geometry("+0+0")

button=tk.Button(win,text="show",command=settext)
entry.pack()
button.pack()


win.mainloop()
