class User:
    def __init__(self, name='', uuid=0):
        self.name = name

        if uuid == 0:
            self.uuid = self.generate_uuid()
        else:
            self.uuid = uuid

    def set_name(self, name):
        self.name = name

    def set_uuid(self, uuid):
        self.uuid = uuid

    def generate_uuid(self):
        return abs(hash(self.name)) % 1000000000

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid

    def get_perm_level(self):
        if 1000000000 < self.uuid < 2000000000:
            return 'Employee'
        elif self.uuid > 2000000000:
            return 'Manager'
        else:
            return 'Customer'

    def display(self):
        """Display function for testing purposes"""
        print(f"Name: {self.name} \nUUID: {self.uuid}")
