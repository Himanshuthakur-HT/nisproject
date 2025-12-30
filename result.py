from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root,text="Add student result",
                      font=("goudy old style", 20, "bold"),
                      bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)
        #====widgets============
        #===========variables=========
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        #========labels and entries======

        self.lbl_select=Label(self.root,text="select student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)       
        self.lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        self.lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        self.lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        self.lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root, textvariable=self.var_roll,values=self.roll_list,font=("goudy old style", 15),state='readonly',justify=CENTER)
        self.txt_student.place(x=280, y=100, width=180)
        self.txt_student.set("Select")
        Button(self.root, text="Search", font=("goudy old style", 15, "bold"),
               bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=470, y=100, width=100, height=28)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=280,y=160,width=290)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=280,y=220,width=290)
        txt_marks_ob=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",15),bg="lightyellow").place(x=280,y=280,width=290)
        txt_full_marks=Entry(self.root,textvariable=self.var_fullmarks,font=("goudy old style",15),bg="lightyellow").place(x=280,y=340,width=290)

        #====button========
        self.btn_add=Button(self.root,text="Submit",font=("times new roman",15,"bold"),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=280,y=420,width=130,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=130,height=35)

        #=====images=====
        self.img_right=Image.open("images/result.jpg")
        self.img_right = self.img_right.resize((500,300), Image.Resampling.LANCZOS)
        self.img_right=ImageTk.PhotoImage(self.img_right)

        self.lbl_img=Label(self.root,image=self.img_right,bg="white",bd=0)
        self.lbl_img.place(x=630,y=100)

#=======================================================================================
    def fetch_roll(self):
        con=sqlite3.connect(database="nis.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database="nis.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def add(self):
        con=sqlite3.connect(database="nis.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="" or self.var_course.get()=="" or self.var_marks.get()=="" or self.var_fullmarks.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())/int(self.var_fullmarks.get()))*100
                    cur.execute("insert into result(roll,name,course,marks_obtained,full_marks,per) values(?,?,?,?,?,?)",
                                (self.var_roll.get(),
                                 self.var_name.get(),
                                 self.var_course.get(),
                                 self.var_marks.get(),
                                 self.var_fullmarks.get(),
                                 str(per)
                                 ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")        

if __name__ == "__main__":
    root = Tk()
    obj = resultclass(root)
    root.mainloop()
