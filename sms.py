from tkinter import *
import time
from tkinter import ttk, messagebox,filedialog
import pymysql
import pandas

def export_data():
    url =filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = Table.get_children()
    newlist = []
    for index in indexing:
        content =Table.item(index)
        datalist = content['values']
        newlist.append(datalist)
    
    table = pandas.DataFrame(newlist,columns=['ID','name','mobile','Email','DOA','Branch','Added date','Added time'])
    table.to_csv(url,index=FALSE)
    messagebox.showinfo('Success!','Data has been exported Succesfully :)')


def iexit():
    result= messagebox.askokcancel('Exit','Do you want to exit out of the app?')
    if result:
        root.destroy()
    else:
        pass 
    


def update_student():
    def update_data():
        query = 'update student set name=%s, mobile=%s,email=%s,DOA=%s,Branch=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(updatestdNameLabelentry.get(),updatestdMobilelabelentry.get(),updatestdEmaillabelentry.get(),updatestdDoalabelentry.get(),updatestdBranchlabelentry.get(),date,currenttime,updatestdIDLabelentry.get()))
        con.commit()
        messagebox.showinfo('Success','Updated the data succesfully :)')
        updatestdwindow.destroy()
        query = 'select * from student'
        mycursor.execute(query)
        fetcheddata =mycursor.fetchall()
        Table.delete(*Table.get_children())
        for data in fetcheddata:
            Table.insert('',END,values=data)


    updatestdwindow = Toplevel()
    updatestdwindow.grab_set()
    updatestdwindow.resizable(0,0)
    updatestdIDlabel = Label(updatestdwindow,text='Id',font=('Arial',12,'bold'))
    updatestdIDlabel.grid(row=0,column=0)
    updatestdIDLabelentry = Entry(updatestdwindow,font=('Arial',12,'bold'),bd=5)
    updatestdIDLabelentry.grid(row=0,column=1)
    updatestdNamelabel = Label(updatestdwindow,text='Name',font=('Arial',12,'bold'))
    updatestdNamelabel.grid(row=1,column=0)
    updatestdNameLabelentry = Entry(updatestdwindow,font=('Arial',12,'bold'))
    updatestdNameLabelentry.grid(row=1,column=1)
    updatestdMobilelabel = Label(updatestdwindow,text='Mobile',font=('Arial',12,'bold'))
    updatestdMobilelabel.grid(row=2,column=0)
    updatestdMobilelabelentry = Entry(updatestdwindow,font=('Arial',12,'bold'))
    updatestdMobilelabelentry.grid(row=2,column=1)
    updatestdEmailLabel = Label(updatestdwindow,text='Email',font=('Arial',12,'bold'))
    updatestdEmailLabel.grid(row=3,column=0)
    updatestdEmaillabelentry = Entry(updatestdwindow,font=('Arial',12,'bold'))
    updatestdEmaillabelentry.grid(row=3,column=1)
    updatestdDoalabel = Label(updatestdwindow,text='DOA',font=('Arial',12,'bold'))
    updatestdDoalabel.grid(row=4,column=0)
    updatestdDoalabelentry =Entry(updatestdwindow,font=('Arial',12,'bold'))
    updatestdDoalabelentry.grid(row=4,column=1)
    updatestdBranchlabel = Label(updatestdwindow,text='Branch',font=('Arial',12,'bold'))
    updatestdBranchlabel.grid(row=5,column=0)
    updatestdBranchlabelentry = Entry(updatestdwindow,font=('Arial',12,'bold'))
    updatestdBranchlabelentry.grid(row=5,column=1)
    updatestdConnectionbutton2 = Button(updatestdwindow,text='UPDATE',font=('Arial,',12,),command=update_data)
    updatestdConnectionbutton2.grid(row=6,column=1) 

    indexing = Table.focus()
    content = Table.item(indexing)
    listdata = content['values']
    updatestdIDLabelentry.insert(0,listdata[0])
    updatestdNameLabelentry.insert(0,listdata[1])
    updatestdMobilelabelentry.insert(0,listdata[2])
    updatestdEmaillabelentry.insert(0,listdata[3])
    updatestdDoalabelentry.insert(0,listdata[4])
    updatestdBranchlabelentry.insert(0,listdata[5])


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    Table.delete(*Table.get_children())
    for data in fetched_data:
        Table.insert('',END,values=data)


def delete_student():
    indexing = Table.focus()
    print(indexing)
    content = Table.item(indexing)
    content_ID = content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_ID)
    con.commit()
    messagebox.showinfo('Success',f'Deleted ID {content_ID}  succesfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    Table.delete(*Table.get_children())
    for data in fetched_data:
        Table.insert('',END,values=data)




def search():
    def search_data():
        query = 'select * from student where id=%s or name=%s or mobile=%s or email=%s or DOA=%s or Branch=%s'
        mycursor.execute(query,(searchIDLabelentry.get(),searchNameLabelentry.get(),searchMobilelabelentry.get(),searchEmaillabelentry.get(),searchDoalabelentry.get(),searchBranchlabelentry.get()))
        Table.delete(*Table.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            Table.insert('',END,values=data)


    searchwindow = Toplevel()
    searchwindow.grab_set()
    searchwindow.resizable(0,0)
    searchwindow.title('SEARCH FOR STUDENT')
    searchIDlabel = Label(searchwindow,text='Id',font=('Arial',12,'bold'))
    searchIDlabel.grid(row=0,column=0)
    searchIDLabelentry = Entry(searchwindow,font=('Arial',12,'bold'),bd=5)
    searchIDLabelentry.grid(row=0,column=1)
    searchNamelabel = Label(searchwindow,text='Name',font=('Arial',12,'bold'))
    searchNamelabel.grid(row=1,column=0)
    searchNameLabelentry = Entry(searchwindow,font=('Arial',12,'bold'))
    searchNameLabelentry.grid(row=1,column=1)
    searchMobilelabel = Label(searchwindow,text='Mobile',font=('Arial',12,'bold'))
    searchMobilelabel.grid(row=2,column=0)
    searchMobilelabelentry = Entry(searchwindow,font=('Arial',12,'bold'))
    searchMobilelabelentry.grid(row=2,column=1)
    searchEmailLabel = Label(searchwindow,text='Email',font=('Arial',12,'bold'))
    searchEmailLabel.grid(row=3,column=0)
    searchEmaillabelentry = Entry(searchwindow,font=('Arial',12,'bold'))
    searchEmaillabelentry.grid(row=3,column=1)
    searchDoalabel = Label(searchwindow,text='DOA',font=('Arial',12,'bold'))
    searchDoalabel.grid(row=4,column=0)
    searchDoalabelentry =Entry(searchwindow,font=('Arial',12,'bold'))
    searchDoalabelentry.grid(row=4,column=1)
    searchBranchlabel = Label(searchwindow,text='Branch',font=('Arial',12,'bold'))
    searchBranchlabel.grid(row=5,column=0)
    searchBranchlabelentry = Entry(searchwindow,font=('Arial',12,'bold'))
    searchBranchlabelentry.grid(row=5,column=1)
    searchConnectionbutton2 = Button(searchwindow,text='SEARCH',font=('Arial,',12,),command=search_data)
    searchConnectionbutton2.grid(row=6,column=1)

def add_student():
    def add_data():
        if IDLabelentry.get()=='' or NameLabelentry.get() =='' or Mobilelabelentry.get()=='' or Emaillabelentry.get()=='' or Doalabelentry.get()=='' or Branchlabelentry.get()=='':
            messagebox.showerror('Invalid','please fill all the detail')
        else:
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%M:%S')
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(IDLabelentry.get(),NameLabelentry.get(),Mobilelabelentry.get(), Emaillabelentry.get(), Doalabelentry.get(), Branchlabelentry.get(),currenttime,currentdate))
            con.commit()
            result=messagebox.askyesno('Success','Do you want to clean up the form?')
            if result:
                IDLabelentry.delete(0,END)
                NameLabelentry.delete(0,END)
                Mobilelabelentry.delete(0,END)
                Emaillabelentry.delete(0,END)
                Doalabelentry.delete(0,END)
                Branchlabelentry.delete(0,END)
            else:
                pass
        

            query = 'select *from student'
            mycursor.execute(query)
            fetcheddata = mycursor.fetchall()
            Table.delete(*Table.get_children())
            for data in fetcheddata:
                Table.insert('',END,values=data)
    

    window = Toplevel()
    window.grab_set()
    window.resizable(0,0)
    IDlabel = Label(window,text='Id',font=('Arial',12,'bold'))
    IDlabel.grid(row=0,column=0)
    IDLabelentry = Entry(window,font=('Arial',12,'bold'),bd=5)
    IDLabelentry.grid(row=0,column=1)
    Namelabel = Label(window,text='Name',font=('Arial',12,'bold'))
    Namelabel.grid(row=1,column=0)
    NameLabelentry = Entry(window,font=('Arial',12,'bold'))
    NameLabelentry.grid(row=1,column=1)
    Mobilelabel = Label(window,text='Mobile',font=('Arial',12,'bold'))
    Mobilelabel.grid(row=2,column=0)
    Mobilelabelentry = Entry(window,font=('Arial',12,'bold'))
    Mobilelabelentry.grid(row=2,column=1)
    EmailLabel = Label(window,text='Email',font=('Arial',12,'bold'))
    EmailLabel.grid(row=3,column=0)
    Emaillabelentry = Entry(window,font=('Arial',12,'bold'))
    Emaillabelentry.grid(row=3,column=1)
    Doalabel = Label(window,text='DOA',font=('Arial',12,'bold'))
    Doalabel.grid(row=4,column=0)
    Doalabelentry =Entry(window,font=('Arial',12,'bold'))
    Doalabelentry.grid(row=4,column=1)
    Branchlabel = Label(window,text='Branch',font=('Arial',12,'bold'))
    Branchlabel.grid(row=5,column=0)
    Branchlabelentry = Entry(window,font=('Arial',12,'bold'))
    Branchlabelentry.grid(row=5,column=1)
    Connectionbutton2 = Button(window,text='Connect',font=('Arial,',12,),command=add_data)
    Connectionbutton2.grid(row=6,column=1)


def connect_database():
    def connect():
        try:
            global mycursor,con
            con = pymysql.connect(host=Hostentry.get(), user=usernameentry.get(), password=Passwordlabelentry.get())
            mycursor = con.cursor()
            messagebox.showinfo("Success", "Database connection is succesful", parent=connectwindow)
        except:
            messagebox.showerror('Error','Invalid details',parent=connectwindow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(id int not null Primary key, name Varchar(30),mobile Varchar(10),email Varchar(100), DOA Varchar(30), Branch Varchar(30),date Varchar(50),time Varchar(50))'
            mycursor.execute(query)
            messagebox.showinfo('Success!' 'Database connectionissuccesful')
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            connectwindow.destroy()
        #Update Student buttons
        
        Addstudentbutton.config(state=NORMAL)
        Searchstudentbutton.config(state=NORMAL)
        Deletestudentbutton.config(state=NORMAL)
        Editstudentbutton.config(state=NORMAL)
        Showstudentbutton.config(state=NORMAL)
        ExportStudentbutton.config(state=NORMAL)


    connectwindow = Toplevel()
    connectwindow.grab_set()
    connectwindow.title('Entry details')
    connectwindow.geometry('470x250+730+230')
    connectwindow.resizable(0, 0)
    Hostlabel = Label(connectwindow, text='Host', font=('Arial', 12, 'bold'))
    Hostlabel.grid(row=0, column=0)
    Hostentry = Entry(connectwindow, font=('Arial', 12, 'bold'))
    Hostentry.grid(row=0, column=1)
    usernamelabel = Label(connectwindow, text='Username', font=('Arial', 12, 'bold'))
    usernamelabel.grid(row=1, column=0)
    usernameentry = Entry(connectwindow, font=('Arial', 12, 'bold'))
    usernameentry.grid(row=1, column=1)
    Passwordlabel = Label(connectwindow, text='password', font=('Arial', 12, 'bold'))
    Passwordlabel.grid(row=2, column=0)
    Passwordlabelentry = Entry(connectwindow, font=('Arial', 12, 'bold'))
    Passwordlabelentry.grid(row=2, column=1)
    Anotherconnectbutton = Button(connectwindow, text='Connect', font=('Arial', 12, 'bold'), command=connect)
    Anotherconnectbutton.grid(row=4, column=0, padx=10, pady=10)


def clock():
    global date,currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    DatetimeLabel.config(text=f'Date{date}\n Time{currenttime}')
    DatetimeLabel.after(300, clock)


root = Tk()
root.title("Student Database System")
root.geometry('1280x720')
root.resizable(0, 0)
DatetimeLabel = Label(root, font=('Arial', 12, 'bold'))
DatetimeLabel.place(x=5, y=5)
clock()

Connectbutton = Button(root, text='Connect to Database', font=('Arial', 12, 'bold'), command=connect_database)
Connectbutton.place(x=1050, y=25)

Rightframe = Frame(root)
Rightframe.place(x=50, y=80, width=300, height=600)

Logoimage = PhotoImage(file='database.png')
LogoimageLabel = Label(Rightframe, image=Logoimage)
LogoimageLabel.grid(row=0, column=0)

# BUTTONS

Addstudentbutton = Button(Rightframe, text="Add student", font=('Arial', 12, 'bold'),command=add_student)
Addstudentbutton.grid(row=1, column=0, padx=10, pady=10)

Editstudentbutton = Button(Rightframe, text="Edit student", font=('Arial', 12, 'bold'),command=update_student)
Editstudentbutton.grid(row=2, column=0, padx=15, pady=15)

Deletestudentbutton = Button(Rightframe, text="Delete student", font=('Arial', 12, 'bold'),command=delete_student)
Deletestudentbutton.grid(row=3, column=0, padx=10, pady=10)

Searchstudentbutton = Button(Rightframe, text="Search student", font=('Arial', 12, 'bold'),command=search)
Searchstudentbutton.grid(row=4, column=0, padx=10, pady=15)

Showstudentbutton = Button(Rightframe, text="Show student", font=('Arial', 12, 'bold'),command=show_student)
Showstudentbutton.grid(row=5, column=0, padx=12, pady=12)

ExportStudentbutton = Button(Rightframe, text="Export student", font=('Arial', 12, 'bold'),command=export_data)
ExportStudentbutton.grid(row=6, column=0, padx=10, pady=12)

exitstudentbutton = Button(Rightframe,text='Exit',font=('Arial',12,'bold'),command=iexit)
exitstudentbutton.grid(row=7,column=0,padx=10,pady=12)

#config

Addstudentbutton.config(state=DISABLED)
Deletestudentbutton.config(state=DISABLED)
Editstudentbutton.config(state=DISABLED)
Searchstudentbutton.config(state=DISABLED)
Showstudentbutton.config(state=DISABLED)
ExportStudentbutton.config(state=DISABLED)

LeftFrame = Frame(root)
LeftFrame.place(x=250, y=80, width=990, height=600)

ScrollbarX = Scrollbar(LeftFrame, orient=HORIZONTAL)
ScrollBarY = Scrollbar(LeftFrame, orient=VERTICAL)

Table = ttk.Treeview(LeftFrame, columns=('Id', 'Name', 'Email', 'Date of Admission', 'Branch', 'Mobile'),
                     xscrollcommand=ScrollbarX.set)

ScrollbarX.config(command=Table.xview)
ScrollBarY.config(command=Table.yview)

ScrollbarX.pack(side=BOTTOM, fill=X)
ScrollBarY.pack(side=RIGHT, fill=Y)

Table.pack(fill=BOTH, expand=1)

Table.heading('Id', text='ID')
Table.config(show='headings')
Table.heading('Name', text='Name')
Table.config(show='headings')
Table.heading('Email', text='Email')
Table.config(show='headings')
Table.heading('Date of Admission', text='Date of Admission')
Table.config(show='headings')
Table.heading('Branch', text='Branch')
Table.config(show='headings')
Table.heading('Mobile', text='Mobile')
Table.config(show='headings')

root.mainloop()

