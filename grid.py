import tkinter as tk
from tkinter import messagebox
def check_user_login():
    txt=User_entry.get()
    pasw=User_password.get()
    name="vasanti"
    pas='1234'
    if(txt==name and pasw==pas):
         messagebox.showinfo("Login Successful","Welcome User")
    else:
        messagebox.showinfo("Login Unsuccessful","Invalid Login Details")
wd=tk.Tk()
wd.title("Grid Geometry Manager")
wd.geometry("500x400")
Label_user_name=tk.Label(wd,text="Username:")
Label_user_name.grid(row=5,column=5,padx=200,pady=10)
User_entry=tk.Entry(wd,width=15)
User_entry.grid(row=7,column=5,padx=200)

Label_password=tk.Label(wd,text="Password:")
Label_password.grid(row=8,column=5,padx=200,pady=10)
User_password=tk.Entry(wd,width=15,show="*")
User_password.grid(row=10,column=5,padx=200)

Login_bt=tk.Button(wd,text="Login",command=check_user_login)
Login_bt.grid(row=11,column=5)
wd.mainloop()