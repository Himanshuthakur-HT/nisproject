from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Manage Student Details",
                      font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ========
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search_by = StringVar()

        # ====== Widgets =======
        #====column1==================
        Label(self.root, text="Roll no", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
       
        Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        self.txt_state = Entry(self.root, textvariable=self.var_state,font=("goudy old style", 15), bg="lightyellow").place(x=150, y=220, width=150)
        
        Label(self.root, text="city", font=("goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        self.txt_city = Entry(self.root, textvariable=self.var_city,font=("goudy old style", 15), bg="lightyellow").place(x=380, y=220, width=100)
        
        Label(self.root, text="pin", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=220)
        self.txt_pin = Entry(self.root, textvariable=self.var_pin,font=("goudy old style", 15), bg="lightyellow").place(x=560, y=220, width=120)
        
       
        Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
       
        self.txt_roll = Entry(self.root, textvariable=self.var_roll,
                                     font=("goudy old style", 15), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=100, width=200)

        txt_email=Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=140, width=200)
        
        self.txt_gender=ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style", 15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        
        #====column2==================
        Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        Label(self.root, text="Addmission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)
        
        #======== Entry Fields ==========
        self.course_list = []
        #function_call to update the list

        self.txt_dob = Entry(self.root, textvariable=self.var_dob,font=("goudy old style", 15), bg="lightyellow").place(x=480, y=60, width=200)

        txt_contact=Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(
            x=480, y=100, width=200)

        txt_addmission=Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15), bg="lightyellow").place(
            x=480, y=140, width=200)
        
        self.txt_course=ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15),state='readonly',justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")
        
        #========text address===========
        self.text_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.text_address.place(x=150, y=260, width=540, height=100)

        # ===== Buttons =====
        self.btn_add = Button(self.root, text="Add", font=("goudy old style", 15, "bold"),
                              bg="#033054", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"),
                                 bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),
                                 bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
                                bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # ===== Search Panel =====
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"),
              bg="white").place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search_by, font=("goudy old style", 15),
              bg="lightyellow").place(x=870, y=60, width=180)

        Button(self.root, text="Search", font=("goudy old style", 15, "bold"),
               bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

        # ===== Table Frame =====
        self.course_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.course_frame.place(x=720, y=100, width=470, height=340)

        scrollx = Scrollbar(self.course_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.course_frame, orient=VERTICAL)

        self.courseTable = ttk.Treeview(self.course_frame, columns=("roll", "name", "email", "gender", "dob","contact","admission","course","state","city","pin","address"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll", text="Roll No.")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("email", text="Email")
        self.courseTable.heading("gender", text="Gender")
        self.courseTable.heading("dob", text="D.O.B")
        self.courseTable.heading("contact", text="Contact")
        self.courseTable.heading("admission", text="Addmission")    
        self.courseTable.heading("course", text="Course")
        self.courseTable.heading("state", text="State")
        self.courseTable.heading("city", text="City")
        self.courseTable.heading("pin", text="Pin")
        self.courseTable.heading("address", text="Address")
        self.courseTable["show"] = "headings"
        self.courseTable.column("roll", width=100)
        self.courseTable.column("name", width=100)
        self.courseTable.column("email", width=150)
        self.courseTable.column("gender", width=100)
        self.courseTable.column("dob", width=100)
        self.courseTable.column("contact", width=100)
        self.courseTable.column("admission", width=100)
        self.courseTable.column("course", width=100)
        self.courseTable.column("state", width=100)
        self.courseTable.column("city", width=100)
        self.courseTable.column("pin", width=100)
        self.courseTable.column("address", width=200)
        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ================= Functions ==============
    def add(self):
        con = sqlite3.connect(database="nis.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Roll No. already exists", parent=self.root)
                else:
                    cur.execute( "INSERT INTO student(roll, name, email, gender, dob, contact, admission, course, state, city, pin, address)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
    (
        self.var_roll.get(),
        self.var_name.get(),
        self.var_email.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_contact.get(),
        self.var_a_date.get(),
        self.var_course.get(),
        self.var_state.get(),
        self.var_city.get(),
        str(self.var_pin.get()),
        self.text_address.get("1.0", END)
    )
)
                    con.commit()                                
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
            
    def show(self):
        con = sqlite3.connect(database="nis.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        cursor = self.courseTable.focus()
        row = self.courseTable.item(cursor)["values"]
        self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.text_description.delete("1.0", END)
        self.text_description.insert(END, row[4])

    def update(self):
        con = sqlite3.connect(database="nis.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Roll No.", parent=self.root)
                else:
                    cur.execute("""UPDATE student SET
                        name=?,
                        email=?,
                        gender=?,
                        dob=?,  
                        contact=?,
                        admission=?,
                        course=?,
                        state=?,
                        city=?,
                        pin=?,
                        address=?
                        WHERE roll=?""",
    (
        self.var_name.get(),
        self.var_email.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_contact.get(),
        self.var_a_date.get(),
        self.var_course.get(),
        self.var_state.get(),
        self.var_city.get(),
        self.var_pin.get(),
        self.text_address.get("1.0", END),
        self.var_roll.get()
    )
)
                    con.commit()                                
                    messagebox.showinfo("Success", "Student Updated Successfully", parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    def delete(self):
        con = sqlite3.connect(database="nis.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Roll No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
                        con.commit()                                
                        messagebox.showinfo("Success", "Student Deleted Successfully", parent=self.root)    
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
                        

    def clear(self):
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.text_description.delete("1.0", END)

    def search(self):
        con = sqlite3.connect(database="nis.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?",(self.var_search_by.get(),))
            rows = cur.fetchone()
            if rows!=None:
               self.courseTable.delete(*self.courseTable.get_children())
               for row in rows:
                self.courseTable.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()
