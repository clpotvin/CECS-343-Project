from user import User


class Customer(User):
    """ Class that represents a customer user

    Attributes:
        name (str): Represents that name of the customer
        uuid (int): A large integer that is hashed from the customer's name (used as a unique identifier)
    """
    def __init__(self, name, uuid):
        """Initializes the customer's name and uuid."""
        super().__init__(name, uuid)

    def set_name(self, name):
        """Changes the users name."""
        super().set_name(name)


    def generate_uuid(self):
        """Generates a new uuid by hashing the customer's name."""
        super().generate_uuid()

    def get_name(self):
        """Returns the customer's name."""
        return self.name

    def get_uuid(self):
        """Returns the customer's uuid"""
        return self.uuid
