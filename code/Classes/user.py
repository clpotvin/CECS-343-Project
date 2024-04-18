class User:
    """ Class that represents a user

        Attributes:
            name (str): Represents that name of the user
            uuid (int): A large integer that is hashed from the user's name (used as a unique identifier)
    """
    def __init__(self, name='', uuid=0):
        """Initializes the user's name and uuid."""

        self.name = name
        if uuid == 0:
            self.uuid = self.generate_uuid()

    def set_name(self, name):
        """Changes the user's name."""
        self.name = name

    def generate_uuid(self):
        """Generates a new uuid by hashing the user's name."""
        return abs(hash(self.name)) % 1000000000

    def get_name(self):
        """Returns the user's name."""
        return self.name

    def get_uuid(self):
        """Returns the user's uuid."""
        return self.uuid

    def display(self):
        """Display function for testing purposes"""
        print(f"Name: {self.name} \nUUID: {self.uuid}")
