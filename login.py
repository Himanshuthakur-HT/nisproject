import sqlite3
from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("900x520+200+120")
        self.root.config(bg="#0f172a")
        self.root.resizable(False, False)

        # ============ Variables ============
        self.email = StringVar()
        self.password = StringVar()

        # ============ Left Panel ============
        left = Frame(self.root, bg="#020617")
        left.place(x=0, y=0, width=400, height=520)

        Label(left, text="Welcome Back!", font=("Segoe UI", 30, "bold"), bg="#020617", fg="#38bdf8").place(x=50, y=150)
        Label(left, text="Login to continue 🚀", font=("Segoe UI", 14), bg="#020617", fg="white").place(x=90, y=220)

        # ============ Right Panel ============
        right = Frame(self.root, bg="white")
        right.place(x=400, y=0, width=500, height=520)

        Label(right, text="Login", font=("Segoe UI", 28, "bold"), bg="white", fg="#020617").place(x=200, y=60)

        # ============ Email ============
        Label(right, text="Email Address", font=("Segoe UI", 11), bg="white", fg="#334155").place(x=80, y=150)
        Entry(right, textvariable=self.email, font=("Segoe UI", 12), bg="#f1f5f9", bd=0).place(x=80, y=175, width=340, height=35)

        # ============ Password ============
        Label(right, text="Password", font=("Segoe UI", 11), bg="white", fg="#334155").place(x=80, y=230)
        Entry(right, textvariable=self.password, font=("Segoe UI", 12), bg="#f1f5f9", show="*", bd=0).place(x=80, y=255, width=340, height=35)

        # ============ Login Button ============
        btn = Button(right, text="LOGIN", command=self.login_user,
                     font=("Segoe UI", 14, "bold"), bg="#0ea5e9", fg="white",
                     activebackground="#0284c7", cursor="hand2", bd=0)
        btn.place(x=140, y=330, width=220, height=45)

    # ============ Login Logic ============
    def login_user(self):
        if self.email.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            con = sqlite3.connect("nis.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                        (self.email.get(), self.password.get()))
            row = cur.fetchone()
            con.close()

            if row is not None:
                messagebox.showinfo("Success", "Login Successful 🎉", parent=self.root)
                # yahan dashboard / home page open kara sakte ho
            else:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        import login
        root = Tk()
        login.Login(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()
