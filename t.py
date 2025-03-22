import tkinter as tk
root=tk.Tk()
root.title("Basic Tkinter window")
root.geometry("500x400")
label=tk.Label(root,text="Welcome")
label.pack()
label.config(text="Welcome to Tkinter! package")
label.pack()
root.mainloop()