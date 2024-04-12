class User:
    def __init__(self, name='', uuid=0):
        self.name = name
        if uuid == 0:
            self.uuid = self.generate_uuid()

    def set_name(self, name):
        self.name = name

    def generate_uuid(self):
        return abs(hash(self.name)) % 1000000000

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid

    def display(self):
        """Display function for testing purposes"""
        print(f"Name: {self.name} \nUUID: {self.uuid}")
