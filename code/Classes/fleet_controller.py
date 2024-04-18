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

    def get_vehicle_index(self, index):
        return self.vehicle_list[index]

    def add_vehicle(self, data):
        temp = Vehicle((data[0][0] + ' ' + data[0][1] + ' ' + data[0][2] + ' ' + data[0][3] + ' ' + data[0][4] + ' ' + data[0][5]))
        arr = data
        arr.append(temp.car_license_plate)
        arr = [arr]
        print(arr)

        df = pd.DataFrame.from_records(arr, columns=["First Name", "Last Name", "Username", "Hashed Password", "UUID"])
        self.vehicle_data = pd.concat([self.vehicle_data, df])
        self.vehicle_data.to_csv(file, mode='w', index=False)
        self.vehicle_data.append(temp)

