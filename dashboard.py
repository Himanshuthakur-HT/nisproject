from dbm import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import math
import time
import random
from course import courseclass
from student import studentclass
from result import resultclass
from report import reportclass
class NIS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # === Base Path ===
        base_path = os.path.join(os.path.dirname(__file__), "images")

        # === Image Paths ===
        logo_path = os.path.join(base_path, "logo_p.png")     # FIXED
        banner_path = os.path.join(base_path, "bg.png")
        user_path = os.path.join(base_path, "result.jpg")

        # === Load Images ===
        self.logo_icon = ImageTk.PhotoImage(Image.open(logo_path).resize((60, 60)))
        self.banner_img = ImageTk.PhotoImage(Image.open(banner_path).resize((900, 350)))
        self.user_icon = ImageTk.PhotoImage(Image.open(user_path).resize((40, 40)))

        # === Top Frame ===
        top = Frame(self.root, bg="#033054", height=90)
        top.pack(fill=X)

        # Logo
        Label(top, image=self.logo_icon, bg="#033054").place(x=20, y=15)

        # Title
        Label(top, text="Student Result Management System",
              font=("goudy old style", 28, "bold"),
              bg="#033054", fg="white").place(x=100, y=22)

        # User Icon (Top Right)
        Label(top, image=self.user_icon, bg="#033054").place(x=1280 - 60, y=15)

        # === Menu Frame ===
        menu_frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15, "bold"),
                                bd=2, relief=RIDGE, bg="white")
        menu_frame.place(x=10, y=100, width=1340, height=80)

        # Buttons List
        
        # === Menu Buttons ===

        btn_Course = Button (menu_frame, text="Course",
                    font=("goudy old style", 15, "bold"),
                    bg="#033054", fg="white",cursor="hand2",command=self.add_course)
        btn_Course.place(x=20, y=5, width=200, height=40)

        btn_Student = Button(menu_frame, text="Student",
                     font=("goudy old style", 15, "bold"),
                     bg="#033054", fg="white",cursor="hand2",command=self.add_student)
        btn_Student.place(x=240, y=5, width=200, height=40)

        btn_Result = Button(menu_frame, text="Result",
                    font=("goudy old style", 15, "bold"),
                    bg="#033054", fg="white",cursor="hand2",command=self.add_result)
        btn_Result.place(x=460, y=5, width=200, height=40)

        btn_View = Button(menu_frame, text="View",
                  font=("goudy old style", 15, "bold"),
                  bg="#033054", fg="white",cursor="hand2",command=self.add_report)
        btn_View.place(x=680, y=5, width=200, height=40)

        btn_Logout = Button(menu_frame, text="Logout",
                    font=("goudy old style", 15, "bold"),
                    bg="#033054", fg="white",)
        btn_Logout.place(x=900, y=5, width=200, height=40)

        btn_Exit = Button(menu_frame, text="Exit",
                  font=("goudy old style", 15, "bold"),
                  bg="#033054", fg="white",command=self.root.quit)
        btn_Exit.place(x=1120, y=5, width=200, height=40)

        # === Banner Image ===
        Label(self.root, image=self.banner_img, bd=2, relief=RIDGE).place(x=350, y=200)

       
        # === Stats Box ===
        self.total_students = 0
        self.total_courses = 0
        self.total_results = 0

        self.make_stats_cards()

        # === Analog Clock ===
        self.make_clock()
        self.update_clock()

    # Dummy Function
    def dummy(self):
        pass

    # === Stats Box Function ===
    def make_stats_cards(self):
        #===update_details===
        self.lbl_student=Label(self.root, text=f"Total Students\n[{self.total_students}]",
                          font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE,
                          bg="#ff5722", fg="white")
        self.lbl_student.place(x=350, y=555, width=300, height=100)

    
        self.lbl_course=Label(self.root, text=f"Total Course\n[{self.total_courses}]",
                          font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE,
                          bg="#1976d2", fg="white")
        self.lbl_course.place(x=650, y=555, width=305, height=100)

        
        self.lbl_result=Label(self.root, text=f"Total Results\n[{self.total_results}]",
                          font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE,
                          bg="#00796b", fg="white")
        self.lbl_result.place(x=955, y=555, width=300, height=100)

    # === Analog Clock ===
    def make_clock(self):
        self.clock_frame = Frame(self.root, bg="black", bd=3, relief=RIDGE)
        self.clock_frame.place(x=10, y=200, width=330, height=320)

        Label(self.clock_frame, text="Analog Clock", font=("times new roman", 20, "bold"),
              fg="white", bg="black").pack()
        self.canvas = Canvas(self.clock_frame, width=300, height=260, bg="black", highlightthickness=0)
        self.canvas.pack()

    def update_clock(self):
        self.canvas.delete("all")

        radius = 120
        center = 150

        self.canvas.create_oval(center - radius, center - radius,
                                center + radius, center + radius,
                                outline="white", width=3)

        # Numeric Positions
        positions = {
            12: (center, center - radius + 20),
            3:  (center + radius - 20, center),
            6:  (center, center + radius - 20),
            9:  (center - radius + 20, center),
        }

        for num, pos in positions.items():
            self.canvas.create_text(pos[0], pos[1], text=str(num), fill="white",
                                    font=("times new roman", 18, "bold"))

        # Clock Hands
        now = time.localtime()
        sec = now.tm_sec
        min_ = now.tm_min
        hr = now.tm_hour % 12

        sec_angle = sec * 6
        min_angle = min_ * 6
        hr_angle = (hr * 30) + (min_ // 2)

        self.draw_hand(center, sec_angle, radius - 30, "red", 2)
        self.draw_hand(center, min_angle, radius - 40, "white", 3)
        self.draw_hand(center, hr_angle, radius - 60, "yellow", 4)

        self.root.after(1000, self.update_clock)

    def draw_hand(self, center, angle, length, color, width):
        x = center + length * (math.sin(angle * 3.14 / 180))
        y = center - length * (math.cos(angle * 3.14 / 180))
        self.canvas.create_line(center, center, x, y, fill=color, width=width)

    def draw_hand(self, center, angle, length, color, width):
        x = center + length * (math.sin(angle * 3.14 / 180))
        y = center - length * (math.cos(angle * 3.14 / 180))
        self.canvas.create_line(center, center, x, y, fill=color, width=width)
        #=================================================================
    def update_details(self):
        con=sqlite3.connect(database="nis.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            student=cur.fetchall()
            self.total_students=len(student)
            self.lbl_student.config(text=f"Total Students\n[{str(len(student))}]")

            cur.execute("select * from course")
            course=cur.fetchall()
            self.total_courses=len(course)
            self.lbl_course.config(text=f"Total Courses\n[{str(len(course))}]")

            cur.execute("select * from result")
            result=cur.fetchall()
            self.total_results=len(result)
            self.lbl_result.config(text=f"Total Results\n[{str(len(result))}]")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)   

    def add_course(self):
        print("Add Course Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = courseclass(self.new_win)

    def add_student(self):
        print("Add Course Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = studentclass(self.new_win)
    
    def add_result(self):
        print("Add Course Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = resultclass(self.new_win)
    
    def add_report(self):
        print("Add Course Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = reportclass(self.new_win)
    

if __name__ == "__main__":
    root = Tk()
    obj = NIS(root)
    root.mainloop()

