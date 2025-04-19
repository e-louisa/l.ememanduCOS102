import os
import csv
import tkinter as tk
from tkinter import messagebox

csv_path = os.path.join(os.path.dirname(__file__), "gig.csv")

def load_employees(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def check_employee():
    name = name_entry.get().strip().lower()
    department = department_entry.get().strip().lower()

    found = False
    other_members = []

    for emp in employees:
        emp_name = emp['Name'].strip().lower()
        emp_dept = emp['Department'].strip().lower()

        if emp_name == name and emp_dept == department:
            found = True
        elif emp_dept == department and emp_name != name:
            other_members.append(emp['Name'])

    if found:
        welcome_message = f"Welcome, {name_entry.get().strip()} from {department_entry.get().strip()} department!"
        if other_members:
            welcome_message += "\n\nOther members in your department:\n- " + "\n- ".join(other_members)
        else:
            welcome_message += "\n\nYou are the only one in your department."
        messagebox.showinfo("Employee Found", welcome_message)
    else:
        messagebox.showwarning("Not Found", f"Sorry, {name_entry.get().strip()} from {department_entry.get().strip()} department is not in our records.")

employees = load_employees(csv_path)

root = tk.Tk()
root.title("GIG Logistics - Employee Verification")

tk.Label(root, text="Enter Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Department:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
department_entry = tk.Entry(root, width=30)
department_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Verify Employee", command=check_employee).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
