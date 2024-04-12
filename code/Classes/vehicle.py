class Vehicle:
    """ A class representing vehicle

    Attributes:
        car_make(str): Make of vehicle
        car_model(str): The model of the vehicle
        car_year (str): The year of the vehicle
        car_trim(str): The trim of the vehicle
        car_license_plate(str): The license number of the vehicle
        price (float): The price of the vehicle
        vehicle_status (str): Current status of the vehicle
    """
    def __init__(self, car_id: int, car_make: str, car_model: str, car_year: int, car_trim: str , car_license_plate: int, price: float, vehicle_status: str):
        self.car_id = car_id
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_trim = car_trim
        self.car_license_plate = car_license_plate
        self.price = price
        self.vehicle_status = vehicle_status

    def set_rental_price(self, price: float):
        """Set the rental price of the vehicle"""
        self.rental_price = price

    def set_status(self, status: str):
        """Set the status of the vehicle"""
        self.status = status

    def get_make(self):
        """Get the make of the vehicle"""
        return self.car_make

    def get_model(self):
        """Get the model of the vehicle"""
        return self.car_model

    def get_year(self):
        """Get the year of the vehicle"""
        return self.car_year

    def get_trim(self):
        """Get the trim of the vehicle"""
        return self.car_trim

    def get_license_plate(self):
        """Get the license plate of the vehicle"""
        return self.car_license_plate

    def get_rental_price(self):
        """Get the rental price of the vehicle"""
        return self.rental_price

    def get_status(self):
        """Get the status of the vehicle"""
        return self.vehicle_status

    def __repr__(self):
        """Returns string of vehicle object in format for file reading/writing"""
        return str(f"{self.car_id},{self.car_make},{self.car_model},{self.car_year},{self.car_trim},"
                   f"{self.car_license_plate},{self.price},{self.vehicle_status}")

