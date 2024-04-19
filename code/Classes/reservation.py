from .vehicle import Vehicle
from datetime import datetime, timedelta


class Reservation:
    def __init__(self, customer_uuid: int, vehicle: Vehicle, reservation_cost: float, start_date: datetime.date,
                 end_date: datetime.date, late_fees: float):
        self.customer_uuid = customer_uuid
        self.vehicle = vehicle
        self.reservation_cost = reservation_cost
        self.start_date = start_date
        self.end_date = end_date
        self.late_fees = late_fees

    def get_customer_uuid(self):
        return self.customer_uuid

    def get_vehicle(self):
        return self.vehicle

    def get_cost(self):
        return self.reservation_cost

    def get_late_fees(self):
        return self.late_fees

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def extend(self, days):
        self.end_date += timedelta(days=days)

