import tkinter as tk
from tkinter import messagebox

class DeliveryPriceCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Delivery Price Checker")
        self.master.geometry("300x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter your delivery location:").pack()
        self.entry_location = tk.Entry(self.master)
        self.entry_location.pack()

        tk.Label(self.master, text="Enter the weight of your delivery:").pack()
        self.entry_weight = tk.Entry(self.master)
        self.entry_weight.pack()

        tk.Button(self.master, text="Check Price", command=self.check_price).pack()

    def check_price(self):
        try:
            weight = int(self.entry_weight.get())
            location = self.entry_location.get().lower()

            if location == "pau":
                if weight >= 10:
                    messagebox.showinfo("Price", "The delivery price is ₦2,000.")
                else:
                    messagebox.showinfo("Price", "The delivery price is ₦1,500.")
            elif location == "epe":
                if weight >= 10:
                    messagebox.showinfo("Price", "The delivery price is ₦5,000.")
                else:
                    messagebox.showinfo("Price", "The delivery price is ₦4,000.")
            else:
                messagebox.showerror("Error", "Unknown location. Please enter 'PAU' or 'Epe'.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for weight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeliveryPriceCheckerApp(root)
    root.mainloop()
