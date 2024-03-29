from user import User


class Employee(User):
    """ Class that represents an employee

    Attributes:
        name (str): Represents that name of the customer
        uuid (int): A large integer that is hashed from the employee's name (used as a unique identifier)
        permission_level (int): Represents the levels of permissions for the employee
    """
    def __init__(self, name, uuid, level):
        """Initializes the employee's name, uuid, and permission level."""
        super().__init__(name, uuid)
        self.permission_level = level

    def set_name(self, name):
        """Changes the employee's name."""
        super().set_name(name)

    def set_permission_level(self, level):
        """Changes the employee's permission level."""
        self.permission_level = level

    def generate_uuid(self):
        """Generates a new uuid by hashing the employee's name."""
        super().generate_uuid()

    def get_name(self):
        """Returns the employee's name."""
        return self.name

    def get_permission_level(self):
        """Returns the employee's permission level."""
        return self.permission_level

    def get_uuid(self):
        """Returns the employee's uuid."""
        return self.uuid

