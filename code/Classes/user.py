class User:
    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid

    def set_name(self, name):
        self.name = name

    def generate_uuid(self):
        self.uuid = abs(hash(self.name))

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid

    def display(self):
        """Display function for testing purposes"""
        print(f"Name: {self.name} \nUUID: {self.uuid}")