from datetime import datetime


class RentalPayment:
    """ Class that represents a rental payment

        Attributes:
            uuid (int): UUID of the customer that made this payment.
            payment_amount (float): Represents the dollar value of the rental payment.
            date (datetime.date): The date of the rental payment.
            reservation (Reservation): Reservation object tied to this payment.
            add_fee (float): Add an additional fee onto the rental payment.
            add_fee_reason (str): Reason for additional fee.
    """
    def __init__(self, uuid: int, payment_amount: float, date: datetime.date, reservation):
        """Initialize the reservation_payment class attributes"""
        self.uuid = uuid
        self.payment_amount = payment_amount
        self.date = date
        self.reservation = reservation
        self.add_fee = 0
        self.add_fee_reason = " "

    def set_additional_fee(self, fee):
        """Set additional fee"""
        self.add_fee = fee

    def set_additional_fee_reason(self, reason):
        """Set reason for the additional fee"""
        self.add_fee_reason = reason

    def get_uuid(self):
        """Get the UUID that is tied to the rental payment"""
        return self.uuid

    def get_payment_amount(self):
        """Get the dollar value of the rental payment"""
        return self.payment_amount

    def get_date_time(self):
        """Get the date of the payment"""
        return self.date

    def get_reservation(self):
        """Get the reservation that is tied to the payment"""
        return self.reservation

    def get_additional_fee(self):
        """Get the additional fees"""
        return self.add_fee

    def get_additional_fee_reason(self):
        """Get the additional fee reason"""
        return self.add_fee_reason
