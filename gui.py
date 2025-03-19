import tkinter as tk
from tkinter import messagebox
def showmsg():
    #print("PRESSED")
    txt=text.get()
    t="hi"+txt
    messagebox.showinfo("text",t)

def showinfo():
    messagebox.showinfo("Info","This is infobox")
def showwarn():
    messagebox.showwarning("Warn","This is warningbox")
def showerr():
    messagebox.showerror("ER","This is error box")

root=tk.Tk()
root.title('GUI APPLICATION')
root.geometry("600x600")

infobt=tk.Button(root,text="Info",command=showinfo)
infobt.pack()

warnbt=tk.Button(root,text="Warn",command=showwarn)
warnbt.pack()

erbt=tk.Button(root,text="Error",command=showerr)
erbt.pack()
lbl=tk.Label(root,text="Enter Name")
lbl.pack()

text=tk.Entry(root,width=10,show="#")
text.pack()

bt=tk.Button(root,text="OK",command=showmsg)
bt.pack()

root.mainloop()