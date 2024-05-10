from datetime import datetime


class ExpensePayment:
    """ Class that represents an expense payment

        Attributes:
            expense_amount (float): Represents the dollar value of the expense
            date (datetime.date): The date of the expense payment
            reason (str): Reason for why expense payment occurred.
    """

    def __init__(self, expense_amount: float, date: datetime.date, reason: str):
        """Initialize the expense_payment class attributes"""
        self.expense_amount = expense_amount
        self.date = date
        self.reason = reason

    def get_expense_amount(self):
        """Get the expense amount"""
        return self.expense_amount

    def get_expense_date(self):
        """Get the expense date"""
        return self.date

    def get_reason(self):
        """Get the reason for the expense"""
        return self.reason

    def set_reason(self, reason):
        """Set the reason for the expense"""
        self.reason = reason

    def set_expense_amount(self, expense_amount):
        """Set the expense amount"""
        self.expense_amount = expense_amount
