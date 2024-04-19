# Handle incoming rental payments and outgoing expense payments
# - Store all data into an excel spreadsheet
# - Spreadsheet should have ongoing total expenses and revenues
# - This class should be able to read from the spreadsheet into a data structure, which can then be used to display in the GUI

from Classes.expense_payment import ExpensePayment
from Classes.rental_payment import RentalPayment
import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))
file1 = os.path.join(current_path,"../Data/Expenses.csv")
file2 = os.path.join(current_path,"../Data/Rentals.csv")



class PaymentController:

    def __init__(self):
        self.expense_data = pd.read_csv(file1)
        self.expenses = [ExpensePayment(n[0], n[1], n[2]) for n in self.expense_data.values]
        self.expense_list = self.expense_data.values.tolist()

        self.rental_data = pd.read_csv(file2)
        self.rentals = [RentalPayment(n[0], n[1], n[2], n[3]) for n in self.rental_data.values]
        self.rental_list = self.rental_data.values.tolist()

    def new_expense(self, data):
        temp = ExpensePayment(data[0], data[1], data[2])
        arr = data
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["Amount", "Date", "Reason"])
        self.expense_data = pd.concat([self.expense_data, df])
        self.expense_data.to_csv(file1, mode='w', index=False)
        self.expenses.append(temp)

    def new_rental(self, data):
        temp = RentalPayment(data[0], data[1], data[2], data[3])
        arr = data
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["UUID", "Amount", "Date", "Reservation"])
        self.rental_data = pd.concat([self.rental_data, df])
        self.rental_data.to_csv(file2, mode='w', index=False)
        self.rentals.append(temp)
