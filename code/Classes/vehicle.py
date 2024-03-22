class Vehicle:
    def __init__(self, car_make: str, car_model: str, car_year: int, car_trim: str , car_license_plate: int, price: float, vehicle_status: str):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_trim = car_trim
        self.car_license_plate = car_license_plate
        self.price = price
        self.vehicle_status = vehicle_status

    def set_rental_price(self, price: float):
        self.rental_price = price

    def set_status(self, status: str):
        self.status = status

    def get_make(self):
        return self.car_make

    def get_model(self):
        return self.car_model

    def get_year(self):
        return self.car_year

    def get_trim(self):
        return self.car_trim

    def get_license_plate(self):
        return self.car_license_plate

    def get_rental_price(self):
        return self.rental_price

    def get_status(self):
        return self.vehicle_status

