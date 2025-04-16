import tkinter as tk
from tkinter import messagebox

#checking weight and location conditions
def check_price():
    try:
        weight = int(entry_weight.get())
        location = entry_location.get().lower()

        if location == "ibejulekki":
            if weight >= 10:
                messagebox.showinfo("Price", "The delivery price is ₦5,000.")
            else:
                messagebox.showinfo("Price", "The delivery price is ₦3,500.")
        elif location == "epe":
            if weight >= 10:
                messagebox.showinfo("Price", "The delivery price is ₦10,000.")
            else:
                messagebox.showinfo("Price", "The delivery price is ₦5,000.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for weight.")

#creating the main window
root = tk.Tk()
root.title("Delivery Price Checker")
root.geometry("300x300")

tk.Label(root, text="Enter your delivery location:").pack()
entry_location = tk.Entry(root)
entry_location.pack()

tk.Label(root, text="Enter the weight of your delivery:").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

#creating the button
tk.Button(root, text="Check Price", command=check_price).pack()

root.mainloop()
