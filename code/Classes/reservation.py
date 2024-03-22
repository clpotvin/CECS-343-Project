from vehicle import Vehicle
from datetime import datetime, timedelta
class Reservation:
    def __init__(self, customer_uuid: int, vehicle: Vehicle, reservation_cost: float, start_time: datetime, end_time: datetime, late_fees: float):
        self.customer_uuid = customer_uuid
        self.vehicle = vehicle
        self.reservation_cost = reservation_cost
        self.start_time = start_time
        self.end_time = end_time
        self.late_fees = late_fees

    def get_customer_uuid(self):
        return self.customer_uuid
    def get_vehicle(self):
        return self.vehicle
    def get_cost(self):
        return self.reservation_cost
    def get_late_fees(self):
        return self.late_fees
    def get_end_time(self):
        return self.end_time
    def add_time(self, days):
        self.end_time += timedelta