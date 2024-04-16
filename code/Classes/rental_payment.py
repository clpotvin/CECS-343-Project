
class RentalPayment:
  def __init__(self, uuid :int, payment_amount: float, date: datetime, reservation: reservation) :
    self.uuid = uuid
    self.payment_amount = payment_amount
    self.date = date
    self.reservation = reservation
    self.add_fee = 0
    self.add_fee_reason = " "
  
  def set_additional_fee(fee: float):
    self.add_fee = fee
  
  def set_additional_fee_reason(reason: string):
    self.add_fee_reason = reason

  def get_uuid():
    return self.uuid

  def get_payment_amount():
    return self.payment_amount

  def get_date_time():
    return self.date

  def get_reservation():
    return self.reservation

  def get_additional_fee():
    return self.add_fee

  def get_additional_fee_reason():
    return self.add_fee_reason


