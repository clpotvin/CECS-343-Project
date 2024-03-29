from user import User


class Customer(User):
    def __init__(self, name, uuid):
        super().__init__(name, uuid)

    def set_name(self, name):
        super().set_name(name)

    def generate_uuid(self):
        super().generate_uuid()

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid
