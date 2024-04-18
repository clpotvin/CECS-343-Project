# This class should manage the vehicles in the fleet, tracking what is available, what is booked, etc.
# - Data should be processed by this class, then stored in an xml file
# - Data might include reservations, current vehicle availability, vehicle damage, etc.
from vehicle import Vehicle
import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(current_path, "../Data/Fleet.csv")

class FleetController:
    def __init__(self):
        self.vehicle_data = pd.read_csv(file)
        self.vehicle_list = self.vehicle_data.values.tolist()
        self.vehicles = [Vehicle(n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7]) for n in self.vehicle_data.values]

    def search_by_plate(self, plate_number):
        for vehicle in self.vehicles:
            if vehicle.car_license_plate == plate_number:
                return vehicle

    def search_by_id(self, id):
        for vehicle in self.vehicles:
            if vehicle.car_id == id:
                return vehicle
        return None

    def get_vehicle_index(self, index):
        return self.vehicle_list[index]

    def add_vehicle(self, data):
        if self.search_by_id(data[0]):
            print("Cannot add vehicle. There is already a vehicle with the existing id.")
            return

        temp = Vehicle(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        data = [data]
        print(data)
        self.vehicles.append(temp)
        print("Adding", data)

        df = pd.DataFrame.from_records(data, columns=["ID", "Make", "Model", "Year", "Trim", "License Plate", "Price", "Status"])
        self.vehicle_data = pd.concat([self.vehicle_data, df])
        self.vehicle_data.to_csv(file, mode='w', index=False)
        self.vehicles.append(temp)

        print("Sucessfully added vehicle.")

