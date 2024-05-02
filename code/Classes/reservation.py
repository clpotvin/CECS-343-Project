from .vehicle import Vehicle
from datetime import datetime, timedelta
class Reservation:
    """ A class representing vehicle

        Attributes:
            customer_uuid (int): a unique set of numbers that are assigned to each customer
            vehicle(vehicle): the vehicle object
            reservation_cost(float): The price to make a reservation
            start_time (datetime): The start time of the reservation
            end_time(datetime): The end time of the reservation
            late_fees(float): the late fees when customer returns the vehicle late
        """
    def __init__(self, customer_uuid: int, vehicle: Vehicle, reservation_cost: float, start_date: datetime.date,
                 end_date: datetime.date, late_fees: float):
        """Initialize the reservation class attributes"""
        self.customer_uuid = customer_uuid
        self.vehicle = vehicle
        self.reservation_cost = reservation_cost
        self.start_date = start_date
        self.end_date = end_date
        self.late_fees = late_fees

    def get_customer_uuid(self):
        """Get the customers unique set of numbers"""
        return self.customer_uuid

    def get_vehicle(self):
        """Get the vehicles that are reserved"""
        return self.vehicle

    def get_cost(self):
        """Get the cost to rent the vehicle"""
        return self.reservation_cost

    def get_late_fees(self):
        """Get the cost to of late fee after returning the vehicle"""
        return self.late_fees

    def get_start_date(self):
        """Get the start time for the reservation"""
        return self.start_date

    def get_end_date(self):
        """Get the end time for the reservation """
        return self.end_date

    def add_time(self, days):
        """Add more time to the reservation"""
        self.end_date += timedelta(days=days)
