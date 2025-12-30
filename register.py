import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("900x520+200+120")
        self.root.config(bg="#0f172a")
        self.root.resizable(False, False)

        # ================= Variables =================
        self.name = StringVar()
        self.email = StringVar()
        self.mobile = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()

        # ================= Left Design =================
        left_frame = Frame(self.root, bg="#020617")
        left_frame.place(x=0, y=0, width=400, height=520)

        Label(left_frame, text="Welcome!", font=("Segoe UI", 30, "bold"), bg="#020617", fg="#38bdf8").place(x=80, y=120)
        Label(left_frame, text="Create your account\nJoin us today 🚀",
              font=("Segoe UI", 14), bg="#020617", fg="white", justify=LEFT).place(x=70, y=200)

        # ================= Right Frame =================
        right_frame = Frame(self.root, bg="white")
        right_frame.place(x=400, y=0, width=500, height=520)

        Label(right_frame, text="Register", font=("Segoe UI", 28, "bold"), bg="white", fg="#020617").place(x=180, y=40)

        # ================= Fields =================
        self.create_field(right_frame, "Full Name", self.name, 120)
        self.create_field(right_frame, "Email Address", self.email, 180)
        self.create_field(right_frame, "Mobile Number", self.mobile, 240)
        self.create_field(right_frame, "Password", self.password, 300, show="*")
        self.create_field(right_frame, "Confirm Password", self.cpassword, 360, show="*")

        # ================= Button =================
        Button(right_frame, text="CREATE ACCOUNT", command=self.register_user,
               font=("Segoe UI", 14, "bold"), bg="#0ea5e9", fg="white",
               activebackground="#0284c7", cursor="hand2", bd=0) .place(x=140, y=430, width=220, height=45)

        self.create_table()

    # ================= Field Creator =================
    def create_field(self, parent, text, var, y, show=None):
        Label(parent, text=text, font=("Segoe UI", 11), bg="white", fg="#334155").place(x=80, y=y)
        Entry(parent, textvariable=var, font=("Segoe UI", 12), bg="#f1f5f9",
              show=show, bd=0).place(x=80, y=y+25, width=340, height=35)

    # ================= Database =================
    def create_table(self):
        con = sqlite3.connect("nis.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE,
                mobile TEXT,
                password TEXT
            )
        """)
        con.commit()
        con.close()

    # ================= Logic =================
    def register_user(self):
        if self.name.get()=="" or self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "Please fill all required fields", parent=self.root)
            return

        if self.password.get() != self.cpassword.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return

        try:
            con = sqlite3.connect("nis.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=?", (self.email.get(),))
            if cur.fetchone():
                messagebox.showerror("Error", "Email already exists", parent=self.root)
            else:
                cur.execute("INSERT INTO users (name,email,mobile,password) VALUES (?,?,?,?)",
                            (self.name.get(), self.email.get(), self.mobile.get(), self.password.get()))
                con.commit()
                messagebox.showinfo("Success", "Account created successfully 🎉", parent=self.root)
                self.clear()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def clear(self):
        self.name.set("")
        self.email.set("")
        self.mobile.set("")
        self.password.set("")
        self.cpassword.set("")


if __name__ == "__main__":
    root = Tk()
    Register(root)
    root.mainloop()