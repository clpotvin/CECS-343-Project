from user import User


class Employee(User):
    def __init__(self, name, uuid, level):
        super().__init__(name, uuid)
        self.permission_level = level

    def set_name(self, name):
        super().set_name(name)

    def set_permission_level(self, level):
        self.permission_level = level

    def generate_uuid(self):
        super().generate_uuid()

    def get_name(self):
        return self.name

    def get_permission_level(self):
        return self.permission_level

    def get_uuid(self):
        return self.uuid

