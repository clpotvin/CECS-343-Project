# This class should manage the vehicles in the fleet, tracking what is available, what is booked, etc.
# - Data should be processed by this class, then stored in an xml file
# - Data might include reservations, current vehicle availability, vehicle damage, etc.
from vehicle import Vehicle
import pandas as pd

class FleetController:
    def __init__(self):
        self.vehicle_data = pd.read_csv("CECS-343-Project/code/Data/view")
        self.vehicles = [Vehicle(n[0], n[1], n[2], n[3], n[4], n[5], n[6]) for n in self.vehicle_data.values]

    def search_by_plate(self, plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate == plate_number:
                return vehicle