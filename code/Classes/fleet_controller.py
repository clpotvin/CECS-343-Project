from .vehicle import Vehicle
from .reservation import Reservation
import datetime
import pandas as pd


def date_str_to_date_obj(date_string) -> datetime.date:
    format_str = '%m-%d-%Y'
    dt = datetime.datetime.strptime(date_string, format_str)
    return dt.date()


class FleetController:
    """Class that represents the fleet of the company

    Attributes:
        vehicle_data (DataFrame): A pandas dataframe containing vehicles in the fleet (from csv)
        vehicles (list): A list containing vehicles in the fleet
        available_vehicles (DataFrame): A pandas dataframe containing only vehicles with 'Available' status.
        reservation_data (DataFrame): A pandas dataframe containing all vehicle reservations (from csv).
        reservations (list): A list containing all reservations as Reservation objects.
    """

    def __init__(self):
        """Initialize an empty list of vehicles."""
        self.vehicle_data = pd.read_csv("CECS-343-Project/code/Data/Vehicles.csv")
        self.vehicles = [Vehicle(n[0], n[1], n[2], n[3], n[4], n[5]) for n in self.vehicle_data.values]
        self.available_vehicles = self.vehicle_data[self.vehicle_data['Status'] == 'Available']
        self.reservation_data = pd.read_csv("CECS-343-Project/code/Data/Reservations.csv")
        self.reservations = [Reservation(n[0], self.search_by_plate(n[1]), n[2], date_str_to_date_obj(n[3]),
                                         date_str_to_date_obj(n[4]), 0) for n in self.reservation_data.values]

    def add_vehicle(self, vehicle):
        """Add vehicle to the list of the fleet"""
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        """Remove vehicle from the list of the fleet"""
        self.vehicles.remove(vehicle)

    def get_available_vehicles(self):
        """Get a list of available vehicles
        Returns:
            list: a list of vehicles that are available to rent
        """
        return [vehicle for vehicle in self.vehicles if vehicle.get_status() == 'Available']

    def rent_vehicle(self, license_plate):
        """Rent a vehicle that matches with its own license plate.

        Returns:
            bool: True if the vehicle is rented. Otherwise, false
        """
        for i in self.vehicles:
            if i.get_license_plate == license_plate and i.get_status() == 'Available':
                i.set_status('Rented')
                return True
        return False

    def return_vehicle(self, license_plate):
        """Returned vehicle that matches with its own license plate.

        Returns:
            bool: True if the vehicle is returned. Otherwise, false
        """
        for i in self.vehicles:
            if i.get_license_plate() == license_plate and i.get_status() == 'Rented':
                i.set_status('Available')
                return True
        return False

    def search_by_plate(self, plate_number):
        """Find and return a vehicle based on its license plate.

        Returns:
            Vehicle: If vehicle is found, return the vehicle.
        """
        for vehicle in self.vehicles:
            if vehicle.license_plate == plate_number:
                return vehicle

    def check_availability(self, license_plate, start_date, end_date):
        start_date_obj = date_str_to_date_obj(start_date)
        end_date_obj = date_str_to_date_obj(end_date)

        if not self.vehicle_data.empty and 'Status' in self.vehicle_data.columns and 'License Plate' in self.vehicle_data.columns:
            if license_plate in self.vehicle_data['License Plate'].tolist():
                idx = self.vehicle_data['License Plate'].tolist().index(license_plate)
                vehicle_status = self.vehicle_data['Status'][idx]
            else:
                return 'Not Available'

        idxs = [x for x in range(0, len(self.reservation_data['License Plate'].tolist())) if
                self.reservation_data['License Plate'][x] == license_plate]

        temp = []
        for i in idxs:
            temp.append([(self.reservation_data['Start Date'][i]),
                         (self.reservation_data['End Date'][i])])
        bookings = pd.DataFrame.from_records(data=temp, columns=['Start Date', 'End Date'])

        for j in bookings.values:
            print(j)
            if start_date_obj <= date_str_to_date_obj(j[0]) <= end_date_obj or start_date_obj <= date_str_to_date_obj(j[1]) <= end_date_obj:
                return 'Not Available'

        return 'Available'
