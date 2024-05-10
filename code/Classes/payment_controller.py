import datetime
from .expense_payment import ExpensePayment
from .rental_payment import RentalPayment
from .vehicle import Vehicle
from .user import User
import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))


class PaymentController:
    """Class that represents the payment system

        Attributes:
            expense_data (DataFrame): A pandas dataframe containing all expense payments (from csv)
            expenses (list): A list containing ExpensePayment objects
            expense_list (list): A list form of the expense_data
            rental_data (DataFrame): A pandas dataframe containing all rental payments (from csv)
            rentals (list): A list containing RentalPayment objects
            rental_list (list): A list form of the rental_data
        """

    def __init__(self):
        """Initialize all class data members."""
        exp = os.path.join(current_path, "../Data/Expenses.csv")
        self.expense_data = pd.read_csv(exp)
        self.expenses = [ExpensePayment(n[0], n[1], n[2]) for n in self.expense_data.values]
        self.expense_list = self.expense_data.values.tolist()

        rnt = os.path.join(current_path, "../Data/Rentals.csv")
        self.rental_data = pd.read_csv(rnt)
        self.rentals = [RentalPayment(n[0], n[1], n[2], n[3]) for n in self.rental_data.values]
        self.rental_list = self.rental_data.values.tolist()

    def new_expense(self, data):
        """Create a new expense payment"""
        exp = os.path.join(current_path, "../Data/Expenses.csv")
        temp = ExpensePayment(data[0], data[1], data[2])
        arr = [[('$' + ("{:.2f}".format(float(data[0])))), data[1], data[2]]]

        df = pd.DataFrame.from_records(arr, columns=["Amount", "Date", "Reason"])
        self.expense_data = pd.concat([self.expense_data, df])
        self.expense_data.to_csv(exp, mode='w', index=False)
        self.expenses.append(temp)

    # method for adding rentals into the csv file
    def new_rental(self, vehicle: Vehicle, user: User, days: int):
        """Create a new rental payment"""
        rnt = os.path.join(current_path, "../Data/Rentals.csv")
        flt = os.path.join(current_path, "../Data/Vehicles.csv")
        fleet = pd.read_csv(flt)
        fleet_list = fleet.values.tolist()

        for idx in range(0, len(fleet.values.tolist()) - 1):
            if vehicle.get_license_plate() == fleet.values.tolist()[idx][4]:
                price = float(fleet_list[idx][5][1:len(fleet_list[idx][5])]) * days
                break

        uuid = user.get_uuid()

        temp = RentalPayment(uuid, price, datetime.datetime.now().date(), vehicle.get_license_plate())
        arr = [uuid, price, datetime.datetime.now().date(), vehicle.get_license_plate()]
        arr = [arr]

        df = pd.DataFrame.from_records(arr, columns=["UUID", "Amount", "Date", "License Plate"])
        self.rental_data = pd.concat([self.rental_data, df])
        self.rental_data.to_csv(rnt, mode='w', index=False)
        self.rentals.append(temp)
        self.rental_list = self.rental_data.values.tolist()


