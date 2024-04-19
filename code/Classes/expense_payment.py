

class ExpensePayment:

  def __init__(self,expense_amount,date,reason):
    self.expense_amount = expense_amount
    self.date = date
    self.reason = reason

  def get_expense_amount(self):
    return self.expense_amount

  def get_expense_date(self):
    return self.date

  def get_reason(self):
    return self.reason

  def set_reason(self,reason):
    self.reason = reason

  def set_expense_amount(self,expense_amount):
    self.expense_amount = expense_amount


  
