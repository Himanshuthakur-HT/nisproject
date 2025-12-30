from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os


class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Manage Course Details",
                      font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ========
        self.var_course_name = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search_by = StringVar()

        # ====== Widgets =======
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        self.txt_course_name = Entry(self.root, textvariable=self.var_course_name,
                                     font=("goudy old style", 15), bg="lightyellow")
        self.txt_course_name.place(x=150, y=60, width=200)

        Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=100, width=200)

        Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=140, width=200)

        self.text_description = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.text_description.place(x=150, y=180, width=500, height=100)

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
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"),
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

        self.courseTable = ttk.Treeview(self.course_frame,
                                        columns=("cid", "name", "duration", "charges", "description"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("cid", text="Course ID")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("duration", text="Duration")
        self.courseTable.heading("charges", text="Charges")
        self.courseTable.heading("description", text="Description")

        self.courseTable["show"] = "headings"

        self.courseTable.column("cid", width=80)
        self.courseTable.column("name", width=100)
        self.courseTable.column("duration", width=100)
        self.courseTable.column("charges", width=100)
        self.courseTable.column("description", width=150)

        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ================= Functions ==============
    def add(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE course_name=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Course already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO course(course_name, duration, charges, description) VALUES(?,?,?,?)",
                                (self.var_course_name.get(),
                                 self.var_duration.get(),
                                 self.var_charges.get(),
                                 self.text_description.get("1.0", END)))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:    
            con.close()
    def show(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
    def get_data(self, ev):
        cursor = self.courseTable.focus()
        row = self.courseTable.item(cursor)["values"]
        self.var_course_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.text_description.delete("1.0", END)
        self.text_description.insert(END, row[4])

    def update(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("UPDATE course SET duration=?, charges=?, description=? WHERE course_name=?",
                            (self.var_duration.get(),
                             self.var_charges.get(),
                             self.text_description.get("1.0", END),
                             self.var_course_name.get()))
                con.commit()
                messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
    def delete(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("DELETE FROM course WHERE course_name=?", (self.var_course_name.get(),))
                con.commit()
                messagebox.showinfo("Success", "Course Deleted Successfully", parent=self.root)
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_course_name.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.text_description.delete("1.0", END)

    def search(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE course_name LIKE ?", ('%' + self.var_search_by.get() + '%',))
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = courseclass(root)
    root.mainloop()
