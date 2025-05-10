import random

employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde",
             "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones", "Nicole Anide", "Kosi Korso",
             "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]

class Employee:

    def __init__(self, name):
        self.name = name

    def check_employee(self):
        if self.name in employees:
            print("Welcome to work, {}.".format(self.name))
            self.take_attendance()
            self.assign_task()
        else:
            self.refuse_access()

    def take_attendance(self):
        print("You have been marked as present today.")

    def assign_task(self):
        task = random.choice(tasks)
        print("Your task for today is: ")
        print(task)
    
    def refuse_access(self):
        print("Access denied. {} is not an employee.".format(self.name))

name_input = input("Enter your name to check in: ")
user = Employee(name_input)
user.check_employee()