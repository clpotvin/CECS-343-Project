
class RentalPayment:
  def __init__(self, uuid :int, payment_amount: float, date, reservation) :
    self.uuid = uuid
    self.payment_amount = payment_amount
    self.date = date
    self.reservation = reservation
    self.add_fee = 0
    self.add_fee_reason = " "
  
  def set_additional_fee(self,fee):
    self.add_fee = fee
  
  def set_additional_fee_reason(self,reason):
    self.add_fee_reason = reason

  def get_uuid(self):
    return self.uuid

  def get_payment_amount(self):
    return self.payment_amount

  def get_date_time(self):
    return self.date

  def get_reservation(self):
    return self.reservation

  def get_additional_fee(self):
    return self.add_fee

  def get_additional_fee_reason(self):
    return self.add_fee_reason


