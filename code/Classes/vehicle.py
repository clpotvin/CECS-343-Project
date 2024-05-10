class Vehicle:
    """ A class representing vehicle

    Attributes:
        make (str): Make of vehicle
        model (str): The model of the vehicle
        year (int): The year of the vehicle
        trim (str): The trim of the vehicle
        license_plate (str): The license number of the vehicle
        price (float): The daily rental price of the vehicle
        status (str): Current status of the vehicle
    """
    def __init__(self, car_make: str, car_model: str, car_trim: str, car_year: int, car_license_plate: int, price: float,
                 vehicle_status: str):
        """Initialize the vehicle class attributes"""
        self.make = car_make
        self.model = car_model
        self.year = car_year
        self.trim = car_trim
        self.license_plate = car_license_plate
        self.price = price
        self.status = vehicle_status

    def set_rental_price(self, price: float):
        """Set the rental price of the vehicle"""
        self.price = price

    def set_status(self, status: str):
        """Set the status of the vehicle"""
        self.status = status

    def get_make(self):
        """Get the make of the vehicle"""
        return self.make

    def get_model(self):
        """Get the model of the vehicle"""
        return self.model

    def get_year(self):
        """Get the year of the vehicle"""
        return self.year

    def get_trim(self):
        """Get the trim of the vehicle"""
        return self.trim

    def get_license_plate(self):
        """Get the license plate of the vehicle"""
        return self.license_plate

    def get_rental_price(self):
        """Get the rental price of the vehicle"""
        return self.price

    def get_status(self):
        """Get the status of the vehicle"""
        return self.status

