import tkinter as tk
from tkinter import messagebox

# Base class
class Zenith:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def check_employee(self):
        return self.name in ["Mary", "Agatha", "Noel"]

    def mutual_services(self):
        return ["Lines of credit", "Insurance", "Investment management and accounts"]

    def unique_services(self):
        return []

# Subclass: Retail Banking
class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ]

# Subclass: Global Banking
class GlobalBanking(Zenith):
    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]

# Subclass: Commercial Banking
class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Advisory services"
        ]

# GUI function
def show_services():
    name = name_entry.get().strip()
    division = division_entry.get().strip().lower()

    if not name or not division:
        messagebox.showerror("Input Error", "Please enter both name and division.")
        return

    employee = None

    # Match division and create appropriate object
    if division == "retail":
        employee = RetailBanking(name)
    elif division == "global":
        employee = GlobalBanking(name)
    elif division == "commercial":
        employee = CommercialBanking(name)
    else:
        messagebox.showerror("Invalid Division", "Please enter a valid division: Retail, Global, or Commercial.")
        return

    if not employee.check_employee():
        messagebox.showerror("Invalid Employee", "Employee not found.")
        return

    mutual = employee.mutual_services()
    unique = employee.unique_services()

    services_text = f"Mutual Services:\n- " + "\n- ".join(mutual)
    if unique:
        services_text += f"\n\nUnique Services for {division.capitalize()} Division:\n- " + "\n- ".join(unique)

    messagebox.showinfo("Services Offered", services_text)

# GUI setup
root = tk.Tk()
root.title("Zenith Bank Services")

tk.Label(root, text="Employee Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Division (Retail / Global / Commercial):").grid(row=1, column=0, padx=10, pady=10)
division_entry = tk.Entry(root)
division_entry.grid(row=1, column=1)

tk.Button(root, text="Show Services", command=show_services).grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()