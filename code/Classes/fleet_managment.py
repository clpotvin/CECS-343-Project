from vehicle import Vehicle
class Fleet_Management:
    """Class that represents the fleet of the company

    Attributes:
         vehicles (list): A list containing vehicles in the fleet
    """
    def __init__(self):
        """Initialize an empty list of vehicles."""
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Add vehicle to the list of the fleet"""
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        """Remove vehicle from the list of the fleet"""
        self.vehicles.remove(vehicle)

    def get_available_vehicle(self):
        """Get a list of available vehicles
        Returns:
            list: a list of vehicles that are available to rent
        """
        return [vehicle for vehicle in self.vehicles if vehicle.get_status()== 'Available']

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
            if i.get_license_plate() == license_plate and vehicle.get_status() == 'Rented':
                i.set_status('Available')
                return True
        return False
