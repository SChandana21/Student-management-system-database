from tkinter import *
from PIL import ImageTk
import tkinter as tk
import ttkthemes
from tkinter import ttk
from tkinter import messagebox

def Buttonlogin():
    if username.get() == '' or Password.get() == '':
        messagebox.showerror("Error", "Fields cannot be empty")
    elif username.get() == 'chandu' and Password.get() == '123':
        messagebox.showinfo('Success','Connected to Database')
        import sms
        window.destroy()
    else:
        messagebox.showerror('Invalid','Wrong username or Password')



window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('adapta')
window.title("Student attendance System")
window.geometry('1280x720')
window.resizable(0,0)
#background image, Label needs to be created
Backgroudimage = ImageTk.PhotoImage(file='image.jpg')
Backgroudimagelabel = Label(window,image=Backgroudimage)
Backgroudimagelabel.place(x=0,y=0)
Newframe = Frame(window)
Newframe.place(x=450,y=350)
username = Entry(Newframe,font=('Arial',15,'bold'))
username.grid(row=0,column=0,padx=10,pady=15)
Password = Entry(Newframe,font=('Arial',15,'bold'))
Password.grid(row=3,column=0,padx=10,pady=10)
Loginbutton = Button(Newframe,font=('Arial',12,'bold'),text='Login',command=Buttonlogin)
Loginbutton.grid(row=5,column=0)

window.mainloop()