from .vehicle import Vehicle
from .reservation import Reservation
import datetime
import pandas as pd


def date_str_to_date_obj(date_string) -> datetime.date:
    """Converts a date string to a datetime.date object and returns the object.

       Returns:
           date (datetime.date): The date as a datetime date object.
    """
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
        """Initialize all class data members."""
        self.vehicle_data = pd.read_csv("CECS-343-Project/code/Data/Vehicles.csv")
        self.vehicles = [Vehicle(n[0], n[1], n[2], n[3], n[4], float(n[5].strip('$')), n[6]) for n in
                         self.vehicle_data.values]
        self.available_vehicles = self.vehicle_data[self.vehicle_data['Status'] == 'Available']
        self.reservation_data = pd.read_csv("CECS-343-Project/code/Data/Reservations.csv")
        self.reservations = [Reservation(n[0], self.search_by_plate(n[1]), n[2], date_str_to_date_obj(n[3]),
                                         date_str_to_date_obj(n[4]), 0) for n in self.reservation_data.values]

    def get_plate_by_index(self, index=-1):
        """Get a vehicle license plate by vehicle index.

        Returns:
            str: vehicle license plate.
        """
        if index == -1:
            return
        current_vehicle = self.vehicles[index]
        if current_vehicle:
            return current_vehicle.license_plate
        else:
            return

    def get_index_by_plate(self, plate=''):
        """Get a vehicle license plate by vehicle index.

        Returns:
            index: vehicle index.
        """
        for idx in range(0, len(self.vehicles)):
            vehicle = self.vehicles[idx]
            if vehicle.license_plate == plate:
                return idx
        return None

    def add_vehicle(self, data):
        """Add a vehicle to the fleet."""
        if self.search_by_plate(data[4]):
            return

        temp = Vehicle(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        data = [data]

        self.vehicles.append(temp)

        df = pd.DataFrame.from_records(data, columns=["Make", "Model", "Trim", "Year", "License Plate", "Daily Rental Price", "Status"])
        self.vehicle_data = pd.concat([self.vehicle_data, df])
        self.vehicle_data.to_csv("CECS-343-Project/code/Data/Vehicles.csv", mode='w', index=False)
        self.vehicles.append(temp)

    def remove_vehicle(self, vehicle):
        """Remove vehicle from the Vehicle object list."""
        self.vehicles.pop(vehicle)

    def delete_vehicle(self, plate):
        """Delete a vehicle from the database and remove it from the Vehicle object list."""
        vehicle = self.search_by_plate(plate)
        if not vehicle:
            return False

        idx = self.get_index_by_plate(plate)
        df = self.vehicle_data
        df = df.drop(idx)
        self.vehicle_data = df
        self.vehicle_data.to_csv("CECS-343-Project/code/Data/Vehicles.csv", mode='w', index=False)
        self.remove_vehicle(idx)
        return True

    def update_vehicle(self, data):
        """Update a vehicle."""
        vehicle = self.search_by_plate(data[4])
        if not vehicle:
            return

        idx = self.get_index_by_plate(data[4])
        self.vehicle_data.loc[idx, 'Make'] = data[0]
        self.vehicle_data.loc[idx, 'Model'] = data[1]
        self.vehicle_data.loc[idx, 'Trim'] = data[2]
        self.vehicle_data.loc[idx, 'Year'] = int(data[3])
        self.vehicle_data.loc[idx, 'Daily Rental Price'] = data[5]
        self.vehicle_data.loc[idx, 'Status'] = data[6]
        self.vehicle_data.to_csv("CECS-343-Project/code/Data/Vehicles.csv", mode='w', index=False)

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
        return None

    def get_availability(self, start_date, end_date):
        """Search through all vehicle statuses and reservations and return a list of vehicles that are available to the specified date range.

        Returns:
             list: List of available vehicles.
        """
        start_date_obj = date_str_to_date_obj(start_date)
        end_date_obj = date_str_to_date_obj(end_date)
        vehicles = []

        if not self.vehicle_data.empty:
            for vehicle in self.vehicle_data.values.tolist():
                if vehicle[6] != 'Maintenance':
                    vehicles.append(vehicle)

            if vehicles:
                for vehicle in vehicles:
                    for reservation in self.reservation_data.values:
                        if vehicle[4] == reservation[1]:
                            if (start_date_obj <= date_str_to_date_obj(reservation[3]) <= end_date_obj or
                                    start_date_obj <= date_str_to_date_obj(reservation[4]) <= end_date_obj):
                                for idx in range(0, len(vehicles) - 1):
                                    v = vehicles[idx]
                                    if v[4] == vehicle[4]:
                                        vehicles.pop(idx)
                return vehicles
        return

    def book_rental(self, uuid, license_plate, start_date, end_date):
        """Book a rental and save it in the reservations data frame, reservation object list, and reservation csv."""
        v = self.vehicle_data.values.tolist()[self.get_index_by_plate(license_plate)]
        cost_float = (date_str_to_date_obj(end_date) - date_str_to_date_obj(start_date)).days * float(v[5][1:len(v[5])])
        cost = '$' + str(cost_float)
        arr = [[uuid, v[4], cost, start_date, end_date]]
        temp = pd.DataFrame.from_records(data=arr, columns=['Customer UUID', 'License Plate', 'Reservation Cost', 'Start Date', 'End Date'])
        self.reservation_data = pd.concat([self.reservation_data, temp])
        self.reservation_data.to_csv("CECS-343-Project/code/Data/Reservations.csv", mode='w', index=False)
        self.reservations.append(Reservation(uuid, self.search_by_plate(v[4]), cost_float, date_str_to_date_obj(start_date), date_str_to_date_obj(end_date), 0))