class Vehicle:
    def __init__(self, car_make: str, car_model: str, car_year: int, car_trim: str, car_license_plate: int,
                 price: float, vehicle_status: str):
        self.make = car_make
        self.model = car_model
        self.year = car_year
        self.trim = car_trim
        self.license_plate = car_license_plate
        self.price = price
        self.status = vehicle_status

    def set_rental_price(self, price: float):
        self.price = price

    def set_status(self, status: str):
        self.status = status

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_trim(self):
        return self.trim

    def get_license_plate(self):
        return self.license_plate

    def get_rental_price(self):
        return self.price

    def get_status(self):
        return self.status
