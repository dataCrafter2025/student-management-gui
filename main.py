import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database create करतो
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()

# Student add करणारी function
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if name and age and grade:
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                       (name, age, grade))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# Student view करणारी function
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    record_str = ""
    for r in records:
        record_str += f"ID: {r[0]}, Name: {r[1]}, Age: {r[2]}, Grade: {r[3]}\n"
    if record_str:
        messagebox.showinfo("Students", record_str)
    else:
        messagebox.showinfo("Students", "No records found.")

# GUI तयार करतो
root = tk.Tk()
root.title("Student Management System")

# Labels आणि Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1, padx=10, pady=5)

# बटणं
tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, pady=10)
tk.Button(root, text="View Students", command=view_students).grid(row=3, column=1, pady=10)

root.mainloop()
