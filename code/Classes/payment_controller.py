# Handle incoming rental payments and outgoing expense payments
# - Store all data into an Excel spreadsheet
# - Spreadsheet should have ongoing total expenses and revenues
# - This class should be able to read from the spreadsheet into a data structure,
# which can then be used to display in the GUI
import datetime
from .expense_payment import ExpensePayment
from .rental_payment import RentalPayment
from .vehicle import Vehicle
from .user import User
import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))


class PaymentController:

    def __init__(self):
        # reads the csv files and creates a list that we can reference to later
        exp = os.path.join(current_path, "../Data/Expenses.csv")
        self.expense_data = pd.read_csv(exp)
        self.expenses = [ExpensePayment(n[0], n[1], n[2]) for n in self.expense_data.values]
        self.expense_list = self.expense_data.values.tolist()

        rnt = os.path.join(current_path, "../Data/Rentals.csv")
        self.rental_data = pd.read_csv(rnt)
        self.rentals = [RentalPayment(n[0], n[1], n[2], n[3]) for n in self.rental_data.values]
        self.rental_list = self.rental_data.values.tolist()

    # method for adding expenses into the csv file
    def new_expense(self, data):
        exp = os.path.join(current_path, "../Data/Expenses.csv")
        temp = ExpensePayment(data[0], data[1], data[2])
        arr = data
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["Amount", "Date", "Reason"])
        self.expense_data = pd.concat([self.expense_data, df])
        self.expense_data.to_csv(exp, mode='w', index=False)
        self.expenses.append(temp)

    # method for adding rentals into the csv file
    def new_rental(self, vehicle, user):
        rnt = os.path.join(current_path, "../Data/Rentals.csv")
        flt = os.path.join(current_path, "../Data/Fleet.csv")
        fleet = pd.read_csv(flt)
        fleet_list = fleet.values.tolist()
        plate = vehicle.get_license_plate()

        for i in fleet_list:
            if plate == fleet_list[i][5]:
                x = i
        uuid = user.get_uuid()
        price = fleet_list[x][6]

        temp = RentalPayment(uuid, price, datetime.datetime.now(), plate)
        arr = [uuid, price, datetime.datetime.now(), plate]
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["UUID", "Amount", "Date", "License Plate"])
        self.rental_data = pd.concat([self.rental_data, df])
        self.rental_data.to_csv(rnt, mode='w', index=False)
        self.rentals.append(temp)
        self.rental_list = self.rental_data.values.tolist()


